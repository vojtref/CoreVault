from machine import Timer, Pin, I2C
import time

# Kruhovy bufferer s lehkym statistickym osetrenim na detekci tepu
class CircularBuffer:
	def __init__(self, size):
		self.data = [0] * size
		self.size = size
		self.pointer = 0

		self.sum = 0

		self.mean = 0
		self.sigma = 0

	def insert(self, n):
		self.sum -= self.data[self.pointer]
		self.sum += n

		self.mean = self.sum / self.size

		self.data[self.pointer] = n
		self.pointer = (self.pointer + 1) % self.size

	def median(self):
		sorteddata = sorted(self.data)
		if self.size % 2 == 0:
			return (sorteddata[self.size // 2] + sorteddata[self.size // 2 + 1]) / 2
		else:
			return sorteddata[self.size // 2]

	# Prumerna absolutni odchylka
	def aad(self):
		tmp = 0
		for x in self.data:
			tmp += abs(x - self.median())
		tmp /= self.size
		return tmp

# Minmax funkce
def clamp(low, value, high):
	return max(low, min(high, value))

# Moje milovana funkcicka pro postupne vykreslovani grafu na prikazovem radku :)
def num_to_bar(num, begin=0, end=65535, width=100):
	begin = max(0, begin)
	end = max(1, end)
	num = clamp(begin, num, end)

	t = width * (num - begin) // (end - begin)

	out = ""
	out += "." * (t)
	out += "#"
	out += "." * (width - t - 1)

	return out

led = Pin("LED", Pin.OUT)

i2c = I2C(id=0, sda=Pin(16), scl=Pin(17), freq=400000)
pulseox = i2c.scan()[0] # Automaticka detekce adresy, predpoklada ze je to jedina I2C periferie


REGISTER_FIFO_CONFIG = 0x08
REGISTER_MODE_CONFIG = 0x09
REGISTER_SPO2_CONFIG = 0x0a

REGISTER_LED1_PA = 0x0c
REGISTER_LED2_PA = 0x0d

i2c.writeto_mem(pulseox, REGISTER_FIFO_CONFIG, bytearray([0b11100000])) # Datasheet str. 17, zvoleny 32x downsampling
i2c.writeto_mem(pulseox, REGISTER_MODE_CONFIG, bytearray([0b00000010])) # Datasheet str. 18, heartbeat mode
i2c.writeto_mem(pulseox, REGISTER_SPO2_CONFIG, bytearray([0b00011000])) # Datasheet str. 18, zvolen raw sample rate 1.6 kS/s (downsampling na 50 S/s)
i2c.writeto_mem(pulseox, REGISTER_LED1_PA, bytearray([0x10])) # Nastavime LED amplitudu (hodnota urcena experimentalne, prilis nizka je zasumena, prilis vysoka peakuje fotosenzor)
i2c.writeto_mem(pulseox, REGISTER_LED2_PA, bytearray([0x00])) # IR LED nechame vyplou

def set_register(add, reg, val):
	i2c.writeto(add, bytearray([reg, val]))

def get_register(add, reg, length=1):
	i2c.writeto(add, bytearray([reg]))
	return i2c.readfrom(add, length)

buffer = CircularBuffer(20)
debounce = CircularBuffer(5) # Debouncing bufferer aby ledka prilis neblikala ze sumu
while True:
	FIFO_WR_POINTER = int.from_bytes(get_register(pulseox, 0x04))
	FIFO_RD_POINTER = int.from_bytes(get_register(pulseox, 0x06))

	num_samples = (FIFO_WR_POINTER - FIFO_RD_POINTER) % 32


	OVF_COUNTER = 0 #int.from_bytes(get_register(pulseox, 0x05))

	for i in range(max(num_samples, OVF_COUNTER)):
		sample_value = int.from_bytes(get_register(pulseox, 0x07, 3))

		# Prilis nizke hodnoty budeme brat jako 0 ("prilis nizke" urceno experimentalne)
		if sample_value < 10000:
			sample_value = 0

		buffer.insert(sample_value)

		deviation = buffer.aad()
		median = buffer.median()

		# Automaticke vycentrovani a zuzeni grafu
		print(num_to_bar(sample_value,
		                 begin=(int(median - 10 * deviation)),
		                 end=(int(median + 10 * deviation)),
		                 width=100),
		      abs(sample_value - median) / max(deviation, 1)) # Pomer odchylky daneho samplu od stredu ku prumerne odchylce

		# Zvazujeme pouze hodnoty vyrazne nizsi, pri tepu se hodnota detekcniho ADC snizuje (okyslicena krev viditelne cervene svetlo lepe absorbuje)
		if -(sample_value - median) > 2 * deviation:
			debounce.insert(1)
		else:
			debounce.insert(0)

		if debounce.sum >= debounce.size / 2: # Pokud debounce buffer prevazne plny, zapneme LED (trochu se tim vyvazi blikani z sumu)
			led.on()
		else:
			led.off()