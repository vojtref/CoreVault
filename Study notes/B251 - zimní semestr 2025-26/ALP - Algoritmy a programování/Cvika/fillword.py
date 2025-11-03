import sys

ws_filepath = sys.argv[1]
dictionary_filepath = sys.argv[2]

directions = ( (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1) )

ws_file = open(ws_filepath)
ws = [l.rstrip("\r\n") for l in ws_file]
ws_h = len(ws)
ws_w = len(ws[0])

dictionary_file = open(dictionary_filepath)
dictionary = [l.rstrip("\r\n") for l in dictionary_file]

# Par jednoduchych vektorovych funkci v Cebysevove prostoru (sachovnicove geometrii) na usnadneni prace, vektor = tuple integeru

def vec_add(vec1, vec2):
	return tuple(a + b for a, b in zip(vec1, vec2))

def vec_sub(vec1, vec2):
	return tuple(a - b for a, b in zip(vec1, vec2))

def vec_scale(n, vec):
	return tuple(n * a for a in vec)

def vec_inv_scale(n, vec):
	return tuple(a // n for a in vec)

def vec_mag(vec):
	return max([abs(a) for a in vec])

def vec_dist(vec1, vec2):
	return vec_mag(vec_sub(vec1, vec2))

def vec_direction(vec1, vec2):
	diff = vec_sub(vec2, vec1)
	mag = vec_mag(diff)
	return vec_inv_scale(mag, diff)

# A par funkci na praci s osmismerkou skrz vektory
# ws = wordsearch

def ws_on_board(vec):
	return vec[0] in range(0, ws_w) and vec[1] in range(0, ws_h)

def ws_char_at_pos(vec):
	if ws_on_board(vec):
		return ws[vec[1]][vec[0]]
	else:
		return None

def ws_nearest_nought(vec, noughts):
	for n in noughts:
		vec_mag(vec_sub(vec, n))

# Check jestli string lezi v danem smeru, a jestli ano, vrati kolik nul proklada, jinak vraci 0
def ws_noughts_in_matching_str(string, p, d):
	found_noughts = 0

	end = vec_add(p, vec_scale(len(string) - 1, d))
	if ws_on_board(end): # Jestli koncova souradnice na osmismerce, checkneme
		for i in range(0, len(string)):
			curr_pos = vec_add(p, vec_scale(i, d))
			curr_char = ws_char_at_pos(curr_pos)
			if curr_char != string[i] and curr_char != "0": # Nalezen rozdil
				return 0
			elif curr_char == "0":
				found_noughts += 1
		return found_noughts # For cyklus pro cely string dokoncen, takze string match
	else: # String saha mimo pole osmismerky, takze tam neni
		return 0

# Prep hotovy, jdeme na to

# Podle rozmeru osmismerky urcime maximalni delku slova, moc dlouha vyradime
max_length = 1 + max(ws_w, ws_h)
dictionary = list(filter(lambda s: len(s) <= max_length, dictionary))

# Vyhledame vsechny nuly
ns = list()
for y in range(ws_h):
	for x in range(ws_w):
		if ws_char_at_pos((x, y)) == "0":
			ns.append((x, y))

# Naivne prokladame primky od prvni nuly, pokud nejaka prolozi vsechny nuly tak ji pouzijeme
colinear = False
for d in range(0, 4):
	found_noughts = 0
	for i in range(-max(ws_w, ws_h), max(ws_w, ws_h)): # Skalujeme i opacne at dostaneme celou primku
		curr_pos = vec_add(ns[0], vec_scale(i, directions[d]))
		curr_char = ws_char_at_pos(curr_pos)

		if curr_char == "0":
			found_noughts += 1
	if found_noughts == len(ns):
		colinear = True
if not colinear:
	print("NONEXIST")
	quit()

# Projdeme vsechny nulove body a najdeme nejvzdalenejsi body od sebe, oznacime si je n_a, n_b
n_a = None
n_b = None
dist = 0
for i in range(0, len(ns)):
	for j in range(0, len(ns)):
		if vec_dist(ns[i], ns[j]) > dist:
			n_a = ns[i]
			n_b = ns[j]
			dist = vec_dist(n_a, n_b)

# Zname body n_a a n_b na primce prochazejici vsemi nulami, takze oznacime vsechny body na primce
points_to_check = list()
for i in range(-max(ws_w, ws_h), max(ws_w, ws_h)):
	d = vec_direction(n_a, n_b)
	curr_pos = vec_add(n_a, vec_scale(i, d))
	if ws_on_board(curr_pos):
		points_to_check.append(curr_pos)

# Body mezi krajnimi odstranime, tzn. odstranime usecku od n_a k n_b vyjma krajnich bodu
for i in range(1, vec_dist(n_a, n_b)):
	d = vec_direction(n_a, n_b)
	p = vec_add(n_a, vec_scale(i, d))
	if p in points_to_check:
		points_to_check.remove(p)

for p in points_to_check:
	# Minimalni delka slova abychom dosahli k n_a, n_b
	min_length = 1 + vec_dist(n_a, n_b) + min(vec_dist(p, n_a), vec_dist(p, n_b))
	# Sla by urcit i maximalni, ale to bych musel pridat funkci na vypocet vzdalenosti od kraje a to se mi fakt nechce
	# Triskam tu nad tim hlavou uz sedmou hodinu, vic uz optimalizovat nechci

	if p == n_a: # Na krajnich bodech chceme smerovat k opacnemu
		d = vec_direction(n_a, n_b)
	elif p == n_b:
		d = vec_direction(n_b, n_a)
	else: # Mimo usecku jsou oba body ve stejnem smeru, tak treba vezmeme n_a
		d = vec_direction(p, n_a)

	for word in dictionary:
		if len(word) < min_length:
			continue # Skipneme moc kratka slova
		elif ws_noughts_in_matching_str(word, p, d) == len(ns): # Prolozime slovo a checkneme jestli prekryva vsechny nuly (redundantni check ze starsi verze)
			print(f"{p[1]} {p[0]} {directions.index(d)} {word}")
			quit()

# Nic nevyslo
print("NONEXIST")

##########
# Okay, BRUTE, je mi to jasny, spatny algoritmus. Necham ho zakomentovany nize jelikoz se mi hrozne libi, geometricky krasny, ale vypocetne neefektivni
##########

## Vyhledame vsechny nuly
#n_coords = list()
#for y in range(ws_h):
#	for x in range(ws_w):
#		if ws_char_at_pos((x, y)) == "0":
#			n_coords.append((x, y))
#
## Slova musi obsahovat alespon jednu nulu (nebyl specifikovan min. pocet), takze z kazde nalezene vysleme paprsky do osmi smeru...
#rays = dict()
#for n in n_coords:
#	rays[n] = set()
#
#	for d in directions:
#		for i in range(0, max(ws_w, ws_h)):
#			p = vec_add(n, vec_scale(i, d))
#			if ws_on_board(p): # Bereme jen body lezici na osmismerce
#				rays[n].add(p)
#
## ...a vezmeme prunik vsech paprsku, na kterem slovo musi lezet
## Pokud nuly nelezi na primkach v danych smerech, vrati prazdnou mnozinu
#points_to_check = list(rays.values())[0] # Odporny, ale s necim zacit musime, a dictview jsou otravny
#for r in rays.values():
#	points_to_check &= r
#
#min_x = min(p[0] for p in n_coords)
#max_x = max(p[0] for p in n_coords)
#
#min_y = min(p[1] for p in n_coords)
#max_y = max(p[1] for p in n_coords)
#
#min_length = max(max_x - min_x, max_y - min_y)
#
#for x, y in points_to_check:
#	for d in directions:
#		if vec_add((x, y), d) not in points_to_check:
#			# Smerujeme mimo body pruniku ve kterem slovo musi lezet, skipujem
#			continue
#
#		for word in dictionary:
#			if len(word) < (min_length - 1):
#				continue
#			if ws_noughts_in_matching_str(word, x, y, d) == len(n_coords): # Slovo je v osmismerce a proklada vsechny nuly
#				print(y, x, directions.index(d), word)
#				quit()
#
## Napada me dost optimalizovanejsich zpusobu, treba urceni smeru podle bodu v pruniku
## (a protismeru, ale to je jen (index + 4) % 8) a vynechani ostatnich,
## nebo cilene prolozeni primky skrz nuly, bylo by to o dost rychlejsi (a asi i prostejsi),
## ale na tom se mi ted nechce delat, navic tohle je o dost zajimavejsi zpusob :P
#
## Pozdejsi verze, BRUTE bezi moc pomalu tak jsem pridal urceni min. delky na prolozeni