def flatten(array):
	result = []
	for i in array:
		if type(i) is list:
			result += flatten(i)
		else:
			result.append(i)
	return result

a=[1, 2, [3, [4, 5], 6, [7]], [8, 9], 10, [11, 12, [13, [14, [15, [16], 17]]]]]

print(flatten(a))