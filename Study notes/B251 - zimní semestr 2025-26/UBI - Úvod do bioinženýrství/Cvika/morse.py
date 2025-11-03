from machine import Pin
import time

dit_length = 100
led_pin = Pin("LED", Pin.OUT)

morse_lut = {
	"A": ".-",
	"B": "-...",
	"C": "-.-.",
	"D": "-..",
	"E": ".",
	"F": "..-.",
	"G": "--.",
	"H": "....",
	"I": "..",
	"J": ".---",
	"K": "-.-",
	"L": ".-..",
	"M": "--",
	"N": "-.",
	"O": "---",
	"P": ".--.",
	"Q": "--.-",
	"R": ".-.",
	"S": "...",
	"T": "-",
	"U": "..-",
	"V": "...-",
	"W": ".--",
	"X": "-..-",
	"Y": "-..-",
	"Z": "-.--",
	"0": "-----",
	"1": ".----",
	"2": "..---",
	"3": "...--",
	"4": "....-",
	"5": ".....",
	"6": "-....",
	"7": "--...",
	"8": "---..",
	"9": "----.",
	".": ".-.-.-",
	",": "--..--",
	"?": "..--..",
	"!": "-.-.--",
	"'": ".---.",
	"/": "-..-.",
}

while True:
	line = input("Enter message: ").upper()

	print("ECHO:", line)
	for c in line:
		if c in morse_lut.keys():
			print(c, morse_lut[c])
			for d in morse_lut[c]:
				led_pin.on()
				if d == ".":
					time.sleep_ms(dit_length)
				elif d == "-":
					time.sleep_ms(dit_length * 3)
				led_pin.off()
				
				time.sleep_ms(dit_length)
			time.sleep_ms(dit_length * 2) # 3 halfbeats total, 1 halfbeat already slept at the end of prev. dit/dah
		elif c == " ":
			print("SPACE")
			time.sleep_ms(dit_length * 4) # 7 halfbeats total, 3 halfbeats already slept at the end of last letter
		else:
			print(c, "INVALID CHAR, SKIPPING")
	print("TRANSMISSION COMPLETED\n")