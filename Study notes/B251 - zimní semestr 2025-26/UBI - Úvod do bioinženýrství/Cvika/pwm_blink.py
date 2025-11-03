from machine import Pin, PWM
import utime

freq = 2
duty = 0.05

pwm = PWM(Pin("LED", Pin.OUT), freq=10000, duty_u16=0)

toggled = False
while True:
	if toggled:
		toggled = False
		pwm.duty_u16(0)
	else:
		toggled = True
		pwm.duty_u16(int(duty * 65535))
	utime.sleep(1 / freq)