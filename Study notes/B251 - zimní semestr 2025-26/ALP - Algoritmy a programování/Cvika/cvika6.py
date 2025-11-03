import sys
import time

#def swapRows(matrix, i, j):
#	tmp = matrix[i].copy()
#	matrix[i] = matrix[j].copy()
#	matrix[j] = tmp.copy()
#	del tmp
#
#M = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
#
#for r in M:
#	print(r)
#
#print("Swapping rows")
#swapRows(M, 0, 2)
#
#for r in M:
#	print(r)

m=[
[0,0,1,0,0,1,0,0,0,0],
[0,0,1,0,0,1,0,0,0,0],
[0,0,1,1,0,1,0,0,0,1],
[0,0,1,0,0,0,1,0,1,0],
[0,0,1,0,0,0,0,1,0,0],
[0,0,1,1,0,1,0,0,0,0],
[0,0,1,0,1,1,1,1,0,0],
[0,0,1,0,0,1,0,1,1,1],
[0,0,1,0,0,1,0,0,0,0],
[0,0,1,0,0,1,0,0,0,0]
]
m_h = len(m)
m_w = len(m[0])

start_coords_str = input().split(" ")[0:2]
start_coords=( int(start_coords_str[0]), int(start_coords_str[1]) )

stack = []
stack.append(start_coords)

history_mem = []

while len(stack) > 0:
	history_mem.append(sys.getsizeof(stack))

	x, y = stack.pop()
	m[y][x] = 2

	for nx, ny in [ (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1) ]:
		if (nx in range(0, m_w) and ny in range(0, m_h)
			and m[ny][nx] == 0 and (nx, ny) not in stack):
				stack.append((nx, ny))

	print()
	for r in m:
		print(r)

	time.sleep(0.5)

print(f"Max stack size: %i bytes" % max(history_mem))
print(f"Avg stack size: %.2f bytes" % (sum(history_mem) / len(history_mem)))
# (4, 4) → LIFO 101.09 bz, FIFO 98.18 b