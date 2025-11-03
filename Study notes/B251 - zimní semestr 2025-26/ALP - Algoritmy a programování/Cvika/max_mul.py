nums = list(map(int, input().split()))

# Asociativni pole, umozni snadne vyhledani offsetu (keys) i delek podposloupnosti (values)
subarray_length_at_offset = dict()

in_subarray = False
for i in range(0, len(nums)):
	if (nums[i] % 3) == 0:
		if in_subarray:
			# Zvysit delku podposloupnosti na poslednim pridanem offsetu (udrzene poradi dle vkladu zaruceno v Python 3.7+, viz https://docs.python.org/3/library/stdtypes.html#dict)
			subarray_length_at_offset[list(subarray_length_at_offset.keys())[-1]] += 1
		else:
			# Pridat dalsi hodnotu (klic = soucasny index), plati pro alespon jedno cislo takze pocatecni hodnota 1
			subarray_length_at_offset[i] = 1
			in_subarray = True
	else:
		in_subarray = False

# Nejvyssi nalezena delka podposloupnosti
# Pokud dict.values() vrati view na prazdne pole (tedy nebyla nalezena zadna podposloupnost), pouzit [0] na vyhnuti se ValueError (max neumi s prazdnym polem pracovat)
maxlen = max(list(subarray_length_at_offset.values()) or [0])

# Pole offsetu vsech podposloupnosti u kterych je delka rovna maxlen
# Pokud maxlen rovno nule, vrati prazdne pole (podposloupnost ma vzdy min 1 prvek)
maxlen_offsets = [k for k,v in subarray_length_at_offset.items() if int(v) == maxlen]

final_offset = 0
final_length = 0
final_sum = 0

# For cyklus pobezi pouze pokud je nejaka nalezena podposloupnost
# Pokud zadna nenalezena (tedy maxlen_offsets prazdne), nepobezi a promenne zustanou nulove
for offset in maxlen_offsets:
	tmp_sum = 0
	for i in range(0, subarray_length_at_offset[offset]):
		tmp_sum += nums[offset + i]
	if final_length == 0 or tmp_sum > final_sum: # Pokud prvni pass (final_length nulove; cyklus bezi, takze podposloupnost existuje, takze delka bude min 1) nebo nova nejvyssi suma, prepsat promenne
		final_offset = offset
		final_length = subarray_length_at_offset[offset]
		final_sum = tmp_sum

print(final_offset, final_length, final_sum)

# Doufam ze dobre okomentovany kod vam neda dojem ze to za me udelal stroj :P
# Jen kdyz muzu vysvetlit, tak proc ne (taky kdo vi jak se v tom vyznam sam za 2 mesice)
# Netusim na cem bezi BRUTE, ale na mem notebooku bezici Python 3.13 do 0.1s zvlada nahodne vstupni posloupnosti o delce >40 000 prvku