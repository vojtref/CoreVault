from machine import Pin, PWM
import utime
import array

freq = 2
lut_size = 100
max_brightness = 8191

pwm_led = PWM(Pin("LED", Pin.OUT), freq=10000, duty_u16=0)

print("Precomputing the LUT")
brightness=array.array("i")
for i in range(lut_size):
	br = int(max_brightness * ((i / (lut_size - 1)) ** 2))
	brightness.append(br)

print("Executing loop")
while True:
	for i in range(lut_size):
		pwm_led.duty_u16(brightness[i])
		utime.sleep((1 / freq) / lut_size)
	for i in range(lut_size):
		pwm_led.duty_u16(brightness[(lut_size - 1) - i])
		utime.sleep((1 / freq) / lut_size)