from machine import Timer, Pin, I2C
import time

# Minmax funkce
def clamp(low, value, high):
	return max(low, min(high, value))

#MAX30102_REGS = { # Datasheet str. 10-11
#	"INT_STAT1": 0x00,
#	"INT_STAT2": 0x01,
#	"INT_EN1": 0x02,
#	"INT_EN2": 0x03,
#	"FIFO_WR_POINTER": 0x04,
#	"OVF_COUNTER": 0x05,
#	"FIFO_RD_POINTER": 0x06,
#	"FIFO_DATA": 0x07,
#	"FIFO_CFG": 0x08,
#	"MODE_CFG": 0x09,
#	"SPO2_CFG": 0x0a,
#
#	"LED1_PA": 0x0c,
#	"LED2_PA": 0x0d,
#
#	"MULTILED_CTR_1": 0x11,
#	"MULTILED_CTR_2": 0x12,
#
#	"DIE_TMP_INT": 0x1f,
#	"DIE_TMP_FRAC": 0x20,
#	"DIE_TMP_CFG": 0x21,
#
#	"REV_ID": 0xfe,
#	"PART_ID": 0xff
#}
#
#MAX30102_MASKS = {
#	"SMP_AVE": 0b11100000,
#	"FIFO_ROLLOVER_EN": 0b00010000,
#	"SHDN": 0b10000000,
#	"RESET": 0b01000000,
#	"MODE": 0b00000011,
#	"SPO2_ADC_RGE": 0b01100000,
#	"SPO2_SR": 0b00011100,
#	"LED_PW": 0b00000011
#}
#
#class MAX30102:
#	def __init__(self, i2c, address=0x00):
#		self.i2c = i2c
#
#		if address == 0x00:
#			self.address = self.i2c.scan()[0]
#		else:
#			self.address = address
#
#	def _i2c_read(self, register, length=1):
#		self.i2c.writeto(self.address, bytearray(register))
#		return int.from_bytes(self.i2c.readfrom(self.address, length))
#
#	def _i2c_write(self, register, data):
#		self.i2c.writeto(self.address, bytearray([register, data]))
#
#	def set_led1_brightness(self, value):
#		if not isinstance(value, int):
#			raise ValueError("value must be of type int")
#		else:
#			clamp(0, value, 0xff)
#			self._i2c_write(MAX30102_REGS["LED1_PA"], value)
#
#	def set_led2_brightness(self, value):
#		if not isinstance(value, int):
#			raise ValueError("value must be of type int")
#		else:
#			clamp(0, value, 0xff)
#			self._i2c_write(MAX30102_REGS["LED2_PA"], value)
#
#	def set_register_field(self, reg, mask, offset, value):
#		if not isinstance(value, int):
#			raise ValueError("value must be of type int")
#		else:
#			clamp(0b00000000, value, mask >> offset)
#
#			print(mask >> offset)
#			reg_val = self._i2c_read(reg)
#			reg_val = (reg_val & (0b11111111 - mask)) | ((value << offset) & mask)
#			self._i2c_write(reg, reg_val)
#
#	# viz datasheet str. 17
#	# 0b000 - 1 (bez zprumerovani)
#	# 0b001 - 2
#	# 0b010 - 4
#	# 0b011 - 8
#	# 0b100 - 16
#	# 0b101 - 32
#	# 0b110 - 32
#	# 0b111 - 32
#	def set_sample_avg(self, value):
#		self.set_register_field(MAX30102_REGS["FIFO_CFG"], MAX30102_MASKS["SMP_AVE"], 5, value)
#
#	def set_fifo_rollover_en(self, value):
#		self.set_register_field(MAX30102_REGS["FIFO_CFG"], MAX30102_MASKS["FIFO_ROLLOVER_EN"], 4, value)
#
#	####
#	# MODE_CFG
#	####
#
#	def set_mode(self, value):
#		if value != 0b010 and value != 0b011 and value != 0b111:
#			raise ValueError(f"Invalid mode: {value}")
#		else:
#			self.set_register_field(MAX30102_REGS["MODE_CFG"], MAX30102_MASKS["MODE"], 0, value)
#
#	####
#	# SPO2_CFG
#	####
#
#	def set_adc_range(self, value):
#		self.set_register_field(MAX30102_REGS["SPO2_CFG"], MAX30102_MASKS["SPO2_ADC_RGE"], 5, value)
#
#	# viz datasheet str. 19
#	# 0b000 - 50
#	# 0b001 - 100
#	# 0b010 - 200
#	# 0b011 - 400
#	# 0b100 - 800
#	# 0b101 - 1000
#	# 0b110 - 1600
#	# 0b111 - 3200
#	def set_sample_rate(self, value):
#		self.set_register_field(MAX30102_REGS["SPO2_CFG"], MAX30102_MASKS["SPO2_SR"], 2, value)
#
#	def set_led_pulsewidth(self, value):
#		self.set_register_field(MAX30102_REGS["SPO2_CFG"], MAX30102_MASKS["LED_PW"], 0, value)
#
#	def read_fifo(self):
#		read_ptr = self._i2c_read(MAX30102_REGS["FIFO_RD_POINTER"])
#		write_ptr = self._i2c_read(MAX30102_REGS["FIFO_WR_POINTER"])
#
#		overflow = self._i2c_read(MAX30102_REGS["OVF_COUNTER"])
#
#		num_samples = max(overflow, (write_ptr - read_ptr) % 32)
#
#		samples = list()
#		for i in range(num_samples):
#			samples.append(self._i2c_read(MAX30102_REGS["FIFO_DATA"], length=3))
#		return samples

# Kruhovy buffer s lehkym statistickym osetrenim na detekci tepu
class CircularBuffer:
	def __init__(self, size):
		self.data = [0] * size
		self.size = size
		self.pointer = 0
		self.sum = 0
		self.mean = 0

	def insert(self, n):
		self.sum += n - self.data[self.pointer]
		self.mean = self.sum / self.size

		self.data[self.pointer] = n
		self.pointer = (self.pointer + 1) % self.size

	def median(self):
		sorteddata = sorted(self.data)
		if self.size % 2 == 0:
			return (sorteddata[self.size // 2] + sorteddata[self.size // 2 + 1]) / 2
		else:
			return sorteddata[self.size // 2]

	# Prumerna absolutni odchylka od medianu
	def aad(self):
		tmp = 0
		for x in self.data:
			tmp += abs(x - self.median())
		tmp /= self.size
		return tmp


class Graphista:
	def __init__(self, begin=0, end=65535, width=100):
		self.begin = begin
		self.end = max(begin+1, end)
		self.width = width
		self.prev_t = 0

	def resize(self, begin=0, end=65535, width=100):
		self.begin = begin
		self.end = max(begin+1, end)
		self.width = width

	def bar(self, num):
		num = clamp(self.begin, num, self.end)

		t = int((self.width - 1) * (num - self.begin) / (self.end - self.begin))
		dt = t - self.prev_t

		out = "|"
		out += " " * min(self.prev_t, t)


		if dt > 0:
			out += "╰" + (abs(dt) - 1) * "─" + "╮"
		elif dt < 0:
			out += "╭" + (abs(dt) - 1) * "─" + "╯"
		else:
			out += "│"
		out += " " * (self.width - max(self.prev_t, t))
		out += "|"

		self.prev_t = t

		del t, dt
		return out


led = Pin("LED", Pin.OUT)

i2c = I2C(id=0, sda=Pin(16), scl=Pin(17), freq=400000)

#pulseox = MAX30102(i2c)
#
#for i in range(0x30):
#	print(f"0x{i:02x}: {pulseox._i2c_read(i):08b}")
#
#
#pulseox.set_mode(0b010)
#pulseox.set_led1_brightness(0x2f)
#
#while True:
#	for s in pulseox.read_fifo():
#		print(s)
#	time.sleep(0.01)

def set_register(add, reg, val):
	i2c.writeto(add, bytearray([reg, val]))

def get_register(add, reg, length=1):
	i2c.writeto(add, bytearray([reg]))
	return i2c.readfrom(add, length)


last_t = 0
bpm = CircularBuffer(5)
def beat_detected():
	global last_t
	global bpm

	curr_t = time.ticks_ms()

	delta_t = curr_t - last_t
	bpm.insert(60000 / delta_t)

	last_t = curr_t
	del delta_t, curr_t

pulseox = i2c.scan()[0] # Automaticka detekce adresy, predpoklada ze je to jedina I2C periferie

REGISTER_FIFO_CONFIG = 0x08
REGISTER_MODE_CONFIG = 0x09
REGISTER_SPO2_CONFIG = 0x0a

REGISTER_LED1_PA = 0x0c
REGISTER_LED2_PA = 0x0d

BRIGHTNESS = 0x4f

set_register(pulseox, REGISTER_FIFO_CONFIG, 0b10100000) # Datasheet str. 17, zvoleny 32x downsampling
set_register(pulseox, REGISTER_MODE_CONFIG, 0b00000010) # Datasheet str. 18, heartbeat mode
set_register(pulseox, REGISTER_SPO2_CONFIG, 0b01110101) # Datasheet str. 18, zvolen raw sample rate 1.6 kS/s (downsampling na 50 S/s)
set_register(pulseox, REGISTER_LED1_PA, BRIGHTNESS)
set_register(pulseox, REGISTER_LED2_PA, 0x00) # IR LED nechame vyplou

print("Measuring baseline...")

baseline_buffer = [0] * 50
baseline_readings = 0
baseline = 0
while baseline_readings < len(baseline_buffer):
	FIFO_WR_POINTER = int.from_bytes(get_register(pulseox, 0x04))
	FIFO_RD_POINTER = int.from_bytes(get_register(pulseox, 0x06))

	OVF_COUNTER = int.from_bytes(get_register(pulseox, 0x05))

	num_samples = max((FIFO_WR_POINTER - FIFO_RD_POINTER) % 32, OVF_COUNTER)

	if num_samples == 0:
		time.sleep(0.01)
	else:
		baseline_buffer[baseline_readings] = int.from_bytes(get_register(pulseox, 0x07, 3))
		baseline_readings += 1
baseline = max(baseline_buffer) * 2
del baseline_buffer, baseline_readings
baseline=10000

print(f"Baseline: {baseline}")

reading_buffer = CircularBuffer(45)
debounce_buffer = CircularBuffer(3)
detected = False
heart = "   "

sample_graphista = Graphista()
signal_graphista = Graphista(begin=0, end=5, width=10)
raw_graphista = Graphista(begin=0, end=0x3fffff, width=100)
while True:
	FIFO_WR_POINTER = int.from_bytes(get_register(pulseox, 0x04))
	FIFO_RD_POINTER = int.from_bytes(get_register(pulseox, 0x06))

	OVF_COUNTER = int.from_bytes(get_register(pulseox, 0x05))

	num_samples = max((FIFO_WR_POINTER - FIFO_RD_POINTER) % 32, OVF_COUNTER)

	if num_samples == 0:
		time.sleep(0.01)
	else:
		for i in range(max(num_samples, OVF_COUNTER)):
			sample_value = int.from_bytes(get_register(pulseox, 0x07, 3))

			## Prilis nizke hodnoty budeme brat jako 0 ("prilis nizke" urceno experimentalne)
			if sample_value < baseline:
				sample_value = 0
				bpm.insert(0)

			buffer_deviation = reading_buffer.aad() or 1
			median = reading_buffer.median() or 1
			buffer_relative_deviation = buffer_deviation / (median or 1)

			sample_deviation = sample_value - median
			sample_relative_deviation = sample_deviation / (median or 1)

			signal = max(0, -(sample_relative_deviation / (buffer_relative_deviation or 1))) # Pri tepu se hodnota z ADC snizuje, zvazujeme pouze levou stranu grafu

			reading_buffer.insert(sample_value)

			debounce_buffer.insert(signal)
			if debounce_buffer.mean > 2:
				if not detected: # Nova detekce tepu
					beat_detected()

					led.on()
					time.sleep(0.002)
					led.off()
				
					heart = " ♥ "
					detected = True
				else:
					heart = "   "
			else:
				heart = "  "
				detected = False

			sample_graphista.resize(begin=(int(median - 10 * buffer_deviation)), end=(int(median + 10 * buffer_deviation)), width=100)
			print(f"{sample_graphista.bar(sample_value)}",
			      f"{signal:8.2f}",
			      f"{signal_graphista.bar(signal)}",
			      f"BPM: {bpm.mean:5.1f}",
			      f"{heart}")

		heart="   "