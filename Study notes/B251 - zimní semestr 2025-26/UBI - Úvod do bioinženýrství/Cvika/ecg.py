from machine import Pin, ADC, Timer

ecg_pin = Pin(26, Pin.IN)
ecg_adc = ADC(ecg_pin)

def clamp(low, value, high):
	return max(low, min(high, value))

def u16_to_bar(u16, begin=0, end=65535, res=256):
	u16 = clamp(0, u16, 65535)

	t = clamp(0, (u16 - begin)/(end - begin), 1)
	n = int(t * res)

	out = "." * res
	out = out[:n] + "#" + out[n+1:]

	del t, n
	return out

def read_and_print(t):
	reading = ecg_adc.read_u16()
	print(u16_to_bar(reading, res=256))

timer = Timer(mode=Timer.PERIODIC, freq=500, callback=read_and_print)
