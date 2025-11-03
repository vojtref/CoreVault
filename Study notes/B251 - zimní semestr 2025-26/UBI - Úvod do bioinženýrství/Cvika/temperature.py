from machine import Pin, PWM, ADC
import utime
import math

pwm = PWM(Pin("LED", Pin.OUT), freq=10000, duty_u16=0)
temp_adc = ADC(4)

print("Measuring baseline reading")
baseline_reading = 0
for i in range(5):
	baseline_reading += temp_adc.read_u16()
	utime.sleep(0.2)
baseline_reading = baseline_reading // 5

print("Executing loop")
while True:
	led_level = -(temp_adc.read_u16() - baseline_reading)/512

	led_level = min(1, led_level)
	led_level = max(0, led_level)

	pwm.duty_u16(int((led_level ** 1.2) * 65535))

	utime.sleep(0.01)