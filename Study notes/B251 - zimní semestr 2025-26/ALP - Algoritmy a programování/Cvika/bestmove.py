import sys

r0 = int(sys.argv[1])
c0 = int(sys.argv[2])
f0 = int(sys.argv[3])
f1 = int(sys.argv[4])
filename = sys.argv[5]

class World:
	def __init__(self, strings):
		self.state = list()
		for line in strings:
			self.state.append(list(map(int, line.split())))

		self.height = len(self.state)
		self.width = len(self.state[0]) # Predpokladame ze vsechny radky byly stejne dlouhe, takze staci checknout prvni

	def __str__(self):
		res = ""
		for row in range(self.height):
			for col in range(self.width):
				val = self.get_tile(row, col)
				if val > 0:
					res += "\033[1;96m"
				elif val < 0:
					res += "\033[1;93m"
				else:
					res += "\033[90m"

				if abs(val) == 1:
					res += "Y"
				elif abs(val) == 2:
					res += "Λ"
				else:
					res += "·"

				res += "\033[0m"
			res += "\n"
		return res

	# Vraci hodnoty policek okolo dane souradnice (nebo None pokud dany smer mimo pole) v tomto poradi:
	# 0: nahoru
	# 1: vpravo nahoru
	# 2: vpravo
	# 3: vpravo dolu
	# 4: dolu
	# 5: vlevo dolu
	# 6: vlevo
	# 7: vlevo nahoru
	def get_surroundings(self, row, col):
		return (self.get_tile(row - 1, col),
		        self.get_tile(row - 1, col + 1),
		        self.get_tile(row, col + 1),
		        self.get_tile(row + 1, col + 1),
		        self.get_tile(row + 1, col),
		        self.get_tile(row + 1, col - 1),
		        self.get_tile(row, col - 1),
		        self.get_tile(row - 1, col - 1))

	def get_tile(self, row, col):
		if self.has_coord(row, col):
			return self.state[row][col]
		else:
			return None

	def has_coord(self, row, col):
		return (row in range(self.height) and
		        col in range(self.width))

world = World([l.strip() for l in open(filename)])

print(world)