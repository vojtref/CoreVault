sums=dict()

for i in range(1000, 10000):
	for ii in range(1, 22):
		for iii in range(22, ii, -1):
			if (ii**3 + iii**3) == i:
				print(i, ii, iii)
				if i in sums:
					sums[i] += 1
				else:
					sums[i] = 1
				if sums[i] == 2:
					exit()