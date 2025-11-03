import sys

class World():
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.contents = list()
		for r in range(0, height):
			self.contents.append(list())
			for c in range(0, width):
				self.contents[r].append(0)

	def __str__(self):
		tmp = ""
		for y in range(0, self.height):
			for x in range(0, self.width):
				if self.get_at(x, y) == 1:
					tmp += "[90m#"
				elif self.get_at(x, y) == 2:
					tmp += "[32m#"
				else:
					tmp += " "
			tmp += "\n"
		tmp += "[0m"
		return tmp

	def has_coord(self, x, y):
		return x in range(0, self.width) and y in range(0, self.height)

	def get_at(self, x, y):
		if self.has_coord(x, y):
			return self.contents[y][x]
		else:
			return None

	def set_at(self, x, y, value):
		if self.has_coord(x, y):
			self.contents[y][x] = value

	def add_wall(self, r1, c1, r2, c2):
		r_start = min(r1, r2)
		r_end = max(r1, r2)
		c_start = min(c1, c2)
		c_end = max(c1, c2)

		for y in range(r_start, r_end + 1):
			for x in range(c_start, c_end + 1):
				self.set_at(x, y, 1)

	def flood_fill_area(self, x, y):
		if self.get_at(x, y) != 0:
			return None

		stack = list()
		stack.append((x, y))

		area = 0
		while len(stack) > 0:
			curr = stack.pop()

			cx, cy = curr
			if self.get_at(cx, cy) == 0:
				area += 1
				self.set_at(cx, cy, 2)

				for nx, ny in [ (cx + 1, cy), (cx, cy - 1), (cx - 1, cy), (cx, cy + 1) ]:
					if self.get_at(nx, ny) == 0:
						stack.append((nx, ny))
		return area

input_file_path = sys.argv[1]
input_file = open(input_file_path)
input_file_contents = [l.rstrip("\r\n") for l in input_file]

world_h, world_w = map(int, input_file_contents[0].split(" "))
world = World(world_w, world_h)

for wall_def_str in input_file_contents[1:]:
	r1, c1, r2, c2 = map(int, wall_def_str.split(" "))
	world.add_wall(r1, c1, r2, c2)

min_area = world.width * world.height
for y in range(0, world.height):
	for x in range(0, world.width):
		if world.get_at(x, y) != 0:
			continue

		tmp_area = world.flood_fill_area(x, y)
		if tmp_area == None:
			continue

		if tmp_area < min_area:
			min_area = tmp_area
print(min_area)
