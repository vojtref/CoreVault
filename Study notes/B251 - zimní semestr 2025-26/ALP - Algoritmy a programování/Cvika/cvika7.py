from fractions import Fraction

def maximum(M, i):
	tmp_j = 0
	tmp_v = 0
	for j in range(0, len(M)):
		if abs(M[j][i]) >= tmp_v:
			tmp_j = j
			tmp_v = abs(M[j][i])
	return tmp_j

def swap_rows(M, i):
	j = maximum(M, i)
	if i != j:
		tmp = M[i].copy()
		M[i] = M[j].copy()
		M[j] = tmp.copy()
		del tmp

def do_line(M, i):
	swap_rows(M, i)
	pivot = M[i][i]

	if pivot != 0:
		for j in range(i, len(M[i])):
			M[i][j] = M[i][j] / pivot

		for r in range(0, len(M)):
			if r == i:
				continue
			mul = M[r][i]
			for s in range(0, len(M[r])):
				M[r][s] -= mul * M[i][s]

		return True
	else:
		return False

def GEM(M):
	for i in range(0, len(M)):
		if not do_line(M, i):
			return False

		print(f"Krok {i}")
		for i in range(len(M)):
			print(M[i])
	return True

m=[[12, -7,  3, 26],
   [ 4,  5, -6, -5],
   [-7,  8,  9, 21]]

m_fr = [list(map(Fraction, v)) for v in m]

print(GEM(m_fr))
for i in range(len(m_fr)):
	print(m_fr[i])