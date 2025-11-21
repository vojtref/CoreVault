import sys
import copy

# Nechapu proc Python nema builtin signum funkci aspon pro integery
# Problemy jsou jen kolem floatu (NaN, +-0) ale integery jsou tak easy
# numpy tady jen kvuli tomuhle importovat nebudu
def sign(num):
	if num > 0:
		return 1
	elif num < 0:
		return -1
	else:
		return 0

# Mohl bych udelat Vec2 class, ale tuples jsou snazsi, proste pouziju funkci ze sveho drivejsiho ukolu fillword.py
def vec_add(vec1, vec2):
	return tuple(a + b for a, b in zip(vec1, vec2))

# Kez by sel cely nas svet dat do jednoho classu, a vsechny zivotni udalosti do (jakz takz) citelnych funkci
# Yoda a Vader to maj tak snadny
class World:
	def __init__(self, strings):
		self.state = list()
		# Tady se fakt hodne spoleham na spravny format vstupniho souboru
		for line in strings:
			self.state.append(list(map(int, line.split())))

		self.height = len(self.state)
		self.width = len(self.state[0]) # Predpokladame ze vsechny radky vstupu byly stejne dlouhe, takze staci checknout prvni

	# Jen neco na pekne vykresleni v terminalu behem testovani
	def __str__(self):
		res = ""
		for row in range(self.height):
			for col in range(self.width):
				curr_coord = (row, col)
				val = self.get_tile(curr_coord)
				# Obarveni pomoci ANSI sekvenci
				if val > 0: # Modra
					res += "\033[1;96m"
				elif val < 0: # Zluta
					res += "\033[1;93m"
				else: # Seda
					res += "\033[90m"

				if abs(val) == 1:
					res += "Y" # Yoda
				elif abs(val) == 2:
					res += "Λ" # Vader
				else: # prazdno
					res += "·"

				# Resetovaci ANSI sekvence
				res += "\033[0m"
			res += "\n"
		return res

	def has_coord(self, coord):
		return coord[0] in range(self.height) and coord[1] in range(self.width)

	def set_tile(self, coord, n):
		if self.has_coord(coord):
			self.state[coord[0]][coord[1]] = n

	def get_tile(self, coord):
		if self.has_coord(coord):
			return self.state[coord[0]][coord[1]]
		else:
			return None

	def get_empty_tiles(self):
		tiles = list()

		for r in range(self.height):
			for c in range(self.width):
				curr_coord = (r, c)
				if self.get_tile(curr_coord) == 0:
					tiles.append(curr_coord)

		return tiles

	def count_same_color_triples(self, figure):
		# Vytvorime si pole do ktereho si vlozime vsechny mozne triplety souradnic
		possible_triples = list()
		for r in range(self.height):
			for c in range(self.height):
				curr_coord = (r, c)
				curr_tile = self.get_tile(curr_coord)
				if sign(curr_tile) == sign(figure): # Nema smysl zacinat na prazdnych polickach ani figurkach jine barvy
					# Trojice nas zajimaji jen rovne a na diagonalach, a jen v jednom smeru
					# Pujdeme svisle, vodorovne, doprava dolu, doleva dolu
					for d in ((1, 0), (0, 1), (1, 1), (1, -1)):
						next_coord = vec_add(curr_coord, d)
						final_coord = vec_add(next_coord, d)
						possible_triples.append((curr_coord, next_coord, final_coord))

		same_color_triples = 0
		for triple in possible_triples:
			same_color_tiles = 0
			for coord in triple:
				curr_tile = self.get_tile(coord)
				if curr_tile == None:
					break # Jsme mimo pole, nema smysl pokracovat se soucasnym tripletem souradnic

				if sign(curr_tile) == sign(figure): # Stejne signum, takze stejna barva
					same_color_tiles += 1
			if same_color_tiles == 3:
				same_color_triples += 1

		del possible_triples # Pro jistotu, aby nebyl memory leak

		return same_color_triples

	def insert_figure(self, coord, figure):
		# Mam chut checknout, zda je dane policko volne, ale slibujete ze je, tak vam duveruju
		# V kodu pro zakaznika by takovahle duvera byla fakt zasadni chyba, nemalokdy se nedrzi ani vlastni dokumentace

		new_world = copy.deepcopy(self)
		new_world.set_tile(coord, figure)

		# Projdeme si osmiokoli
		for d in ((-1, 0), # Nahoru
		          (-1, 1), # Nahoru doprava
		          (0, 1), # Doprava
		          (1, 1), # Doprava dolu
		          (1, 0), # Dolu
		          (1, -1), # Doleva dolu
		          (0, -1), # Doleva
		          (-1, -1)): # Doleva nahoru
			checked_coord = vec_add(coord, d)
			checked_tile = new_world.get_tile(checked_coord)
			if checked_tile == 0 or checked_tile == None: # Skipneme prazdna policka a policka mimo herni pole
				continue
			elif abs(checked_tile) <= abs(figure): # Yoda odpuzuje jen sebe, Vader odpuzuje Yodu i sebe (Vader i Yoda potrebujou vyssi sebevedomi, chudaci)
				push_coord = vec_add(checked_coord, d) # Opet se posuneme ve stejnem smeru
				if new_world.get_tile(push_coord) == None: # Pokud posouvame mimo herni pole, figurka prestane existovat
					new_world.set_tile(checked_coord, 0)
				if new_world.get_tile(push_coord) == 0: # Policko na ktere ma byt figurka odpuzena je na hernim poli a je prazdne
					new_world.set_tile(checked_coord, 0)
					new_world.set_tile(push_coord, checked_tile)

		return new_world

	# Kez by nam svet dal funkci ktera nam rekne ten nejlepsi tah
	# I kdyz s tim jak to tu odporne bruteforceuju je mozna lepsi ze takova funkce neni,
	# pro tak komplexni hru jako zivot by byla napsana jeste hur
	#
	# Tohle by slo snadno upravit aby to rekurzivne i minimalizovalo protihracovy sance,
	# tj. aby protihracovi opacne barvy dalsi tah dal co nejmene trojic,
	# slo by tim zpusobem i snadno prochazet tahy do dane hloubky,
	# ale nebyly dostatecne definovany pravidla hry abych vedel ze tak hra fakt funguje,
	# a tenhle bruteforce approach by na to byl fakt spatny
	def get_best_placement(self, figure):
		best_coord = None
		best_triple_count = 0
		for coord in self.get_empty_tiles():
			new_world = self.insert_figure(coord, figure)

			curr_triple_count = new_world.count_same_color_triples(figure)

			if  curr_triple_count > best_triple_count:
				best_triple_count = curr_triple_count
				best_coord = coord

		return best_coord

# Ted konecne runtime, yay
if __name__ == '__main__':
	r0 = int(sys.argv[1])
	c0 = int(sys.argv[2])
	f0 = int(sys.argv[3])
	f1 = int(sys.argv[4])
	filename = sys.argv[5]

	world = World([l for l in open(filename)])

	new_world = world.insert_figure((r0, c0), f0)

	best_coord = new_world.get_best_placement(f1)

	print(f"{best_coord[0]} {best_coord[1]}")