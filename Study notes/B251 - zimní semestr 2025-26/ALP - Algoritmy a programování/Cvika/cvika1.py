#!/usr/bin/python3

#print(2**500 + 10)
#print(2**500 + 10.0)
#print(2**500 + 0.0)
#print(2**500 + 10.0 == 2**500 + 0.0)

# a = (a//b)*b + (a%b)
#print(10//-3) # -4
#print(10%-3) # -2

for i in range(1, 20):
	divisible = False
	if i % 3 == 0:
		print("Fizz", end="")
		divisible = True
	if i % 5 == 0:
		print("Buzz", end="")
		divisible = True

	if not divisible:
		print(i, end="")
	print()
