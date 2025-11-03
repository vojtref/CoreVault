from re import split as re_split

equation_in = input()

expression = equation_in.split('=')[0].strip() # Leva strana rovnice, retezec
value = equation_in.split('=')[1].strip() # Prava strana rovnice, x
# strip dle formatu specifikovanem v zadani neni potreba, ale je to dobra hygiena

tokenized_expr = re_split(r"([-+*/])", expression) # Token bud cislo nebo operator
# Dle formatu urceneho v zadani budou sude pozice cisla, liche pozice operatory

# Prevod pole stringu na jeden string (detokenizace)
def strlist_to_str(list, sep=""):
	return sep.join(list)

# Wrapper pro eval na pole stringu
def eval_strlist(strlist):
	return eval(strlist_to_str(strlist))

for i in range(0, len(tokenized_expr), 2):
	for ii in range(i + 1, len(tokenized_expr) + 1, 2):
		# Zkusime pridat zavorky
		# Pridame od konce, abychom nemuseli resit zmeny indexu
		tokenized_expr.insert(ii, ")")
		tokenized_expr.insert(i, "(")

		# Urcime hodnotu noveho vyrazu
		# Formatjeme jako string s presnosti na 5 desetinnych mist, dle zadani
		curr_val = "%.5f" % eval_strlist(tokenized_expr)

		# Oba stringy s platnym formatem, muzeme porovnat rovnou
		if curr_val == value:
			# Pokus vysel, napsat vyslednou rovnici a ukoncit
			# Opravena verze ktera pred a za rovnitkem nepise mezeru
			print(f"{strlist_to_str(tokenized_expr)}={value}")
			exit()
		else:
			# Tento pokus nevysel, odebrat vlozene zavorky
			# Odebirame od zacatku, opet abychom neresili indexy
			tokenized_expr.pop(i) # (
			tokenized_expr.pop(ii) # )

# Ani jeden pokus vlozeni zavorek neudelal rovnici platnou (jinak by se program ukoncil), takze nelze
print("NELZE")