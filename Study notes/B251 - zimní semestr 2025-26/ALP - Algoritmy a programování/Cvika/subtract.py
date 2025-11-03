import math

str_a = input()
base_a = int(input())
str_b = input()
base_b = int(input())
base_out = int(input())

chars="0123456789abcdefghijklmnopqrstuvwxyz"

def str_to_n(str_in, base):
	# Podvlakno s povolenymi znaky dane soustavy
	possible_chars = chars[0:base]

	tmp_val=0
	for i in range(0, len(str_in)):
		char_val=possible_chars.find(str_in[::-1][i]) # Zaciname od 0, takze vlakno je treba prochazet pozpatku jelikoz je little endian
		if char_val == -1: # Znak neni mezi povolenymi
			print("ERROR")
			exit()
		else:
			tmp_val += char_val * (base ** i)
	return tmp_val

def n_to_str(n, base):
	tmp_str = ""

	max_pow = int(math.log(n or 1, base))

	for i in range(max_pow, -1, -1): # Od nejvetsi mocniny po nejmensi
		tmp_str += chars[(n % (base ** (i + 1))) // (base ** i)]
	return tmp_str

a = str_to_n(str_a, base_a)
b = str_to_n(str_b, base_b)

print(n_to_str(abs(a - b), base_out))