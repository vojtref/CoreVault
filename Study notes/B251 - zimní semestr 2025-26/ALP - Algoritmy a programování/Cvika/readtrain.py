# Trosku citelnejsi verze :P

import sys

trains_correct_filepath = sys.argv[1]
trains_corrupt_filepath = sys.argv[2]

# Vypocet rozdilnosti dvou stringu
def string_diff(corrupt, correct):
	differences = 0
	if (len(corrupt) != len(correct)):
		differences=100 # Pokud je mezi stringy rozdilna delka, rozdilnost je rovna 100, jak specifikovano v zadani
	else:
		for i in range(0, len(corrupt)): # Prochazeni obou stringu znak po znaku
			if corrupt[i] != correct[i]: # Pro kazdy rozdilny znak zvysit differences o 1
				differences += 1
	return differences

# Vraci nejpodobnejsi string z pole
# corrupt - string ktery chceme opravit
# correct_list - pole moznych spravnych stringu (v teto uloze jmena stanic, casy)
def find_most_similar(corrupt, correct_list):
	diff_of_name = dict() # Asociativni pole, keys - jmena spravnych stringu, value - rozdilnost od porovnavaneho stringu
	for correct in correct_list:
		diff_of_name[correct] = string_diff(corrupt, correct)
	return min(diff_of_name, key=diff_of_name.get) # Vratit string ze spravnych ktery ma nejnizsi rozdilnost (tj. je nejblize porovnavanemu stringu)

# Asociativni pole spravne napsanych vlaku
# key - jmeno destinace vlaku
# value - pole casu odjezdu do dane destinace
trains_correct = dict()

# Precteme spravna jmena stanic a odjezdy ze souboru
with open(trains_correct_filepath) as trains_correct_file:
	for line in trains_correct_file:
		line_split=line.strip().split(';') # Rozdelit jmeno a casy strednikem

		train_destination = line_split[0].strip() # Odebereme prebytecne mezery z destinace (vc. vyplnujicich na 31 znaku)
		train_times = line_split[1].strip().split(' ') # Odebereme prebytecne mezery pred a za casy, pote rozdelime casy oddelene mezerou na pole

		trains_correct[train_destination] = train_times # Asociace jmena destinace a pole casu odjezdu do dane destinace

# Precteme tabuli a za letu opravime
with open(trains_corrupt_filepath) as trains_corrupt_file:
	for line in trains_corrupt_file:
		# Extrakce dat z kazdeho radku tabule dle specifikovaneho formatu
		train_corrupt_destination = line[0:30].rstrip() # Odebereme vyplnujici mezery
		train_corrupt_code = line[32:35]
		train_corrupt_time = line[37:42]

		train_destination = find_most_similar(train_corrupt_destination, trains_correct.keys()) # Prelozeni zkomoleneho jmena destinace vlaku na nejblizsi spravne
		train_time = find_most_similar(train_corrupt_time, trains_correct[train_destination]) # Prelozeni zkomoleneho casu na nejblizsi spravny cas vlaku do prislusne destinace

		print(f"{train_destination}, {train_time}")