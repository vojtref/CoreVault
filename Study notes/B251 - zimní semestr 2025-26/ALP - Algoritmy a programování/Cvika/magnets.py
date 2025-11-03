import sys

filepath = sys.argv[1]

input_file = open(filepath)
# Pole vsech radku, s odstranenymi CR a NL
input_file_lines = [line.rstrip('\r\n') for line in input_file]

new_magnet_polarity = input_file_lines[0].strip()
new_magnet_position = tuple(input_file_lines[1].strip().split(" "))

new_x = int(new_magnet_position[0])
new_y = int(new_magnet_position[1])

# Sestaveni hraciho pole
board = list()
for line in input_file_lines[2:]:
	new_row = list()
	for i in range(0, len(line)):
		new_row.append(line[i])
	board.append(new_row)

if (
	(new_y not in range(0, len(board))) or # Overime ze souradnice jsou na hracim poli
	(new_x not in range(0, len(board[0]))) or
	(board[new_y][new_x] != " ") # ...a ze policko prazdne
   ): # Pokud ne, error
	print("ERROR")
	exit()

new_board = list(board) # Zkopirujeme pole
new_board[new_y][new_x] = new_magnet_polarity # Vlozime novy magnet (uz overeno ze tam nic neni)

# Signum, bude uzitecne
# Nebude zvladat NaN, ale na to tu nenarazime, pracujeme tu jen s integery
def sgn(n):
	if n > 0:
		return 1
	if n < 0:
		return -1
	return 0

# Nasleduje odpornost kterou rozhodne jde nejak sloucit do jedny pekny funkce,
# patrny z toho jak moc se kod opakuje, ale ted me nenapada jak
# Mozna to udelam pozdeji, ale prozatim chci hlavne mit neco funkcniho na odevzdani

# Odpuzovani
for j in (-1, 0, 1):
	for i in (-1, 0, 1):
		x = new_x + i
		y = new_y + j
		if (
			(i == 0 and j == 0) or # Preskocime totozne policko
			(x not in range(0, len(board[0]))) or # Preskocime hodnoty mimo pole
			(y not in range(0, len(board))) or
			(board[y][x] == " ") or # Preskocime prazdna policka
			(board[y][x] != new_magnet_polarity) # Preskocime odlisnou polaritu (ted pouze odpuzujeme)
		   ):
			continue

		target_x = x + sgn(i)
		target_y = y + sgn(j)

		if (target_x in range(0, len(new_board[0]))) and (target_y in range(0, len(new_board))):
			if new_board[target_y][target_x] != " ": # Pokud tam uz neco je, nic nedelame
				continue
			else:
				new_board[target_y][target_x] = board[y][x]
				new_board[y][x] = " "
		else: # Cilove policko mimo hraci pole, jen odstranime
			new_board[y][x] = " "

# Pritahovani
for j in (-2, 0, 2):
	for i in (-2, 0, 2):
		x = new_x + i
		y = new_y + j
		if (
			(i == 0 and j == 0) or # Preskocime totozne policko
			(x not in range(0, len(board[0]))) or # Preskocime hodnoty mimo pole
			(y not in range(0, len(board))) or
			(board[y][x] == " ") or # Preskocime prazdna policka
			(board[y][x] == new_magnet_polarity) # Preskocime stejnou polaritu (ted pouze pritahujeme)
		   ):
			continue

		target_x = x - sgn(i)
		target_y = y - sgn(j)

		if (target_x in range(0, len(board[0]))) and (target_y in range(0, len(board))):
			if new_board[target_y][target_x] != " ": # Pokud tam uz neco je, nic nedelame
				continue
			else:
				new_board[target_y][target_x] = board[y][x]
				new_board[y][x] = " "
		else: # Cilove policko mimo hraci pole, jen odstranime
			new_board[y][x] = " "

for i in range(len(new_board)):
	for j in range(len(new_board[i])):
		print(new_board[i][j], end="")
	print()