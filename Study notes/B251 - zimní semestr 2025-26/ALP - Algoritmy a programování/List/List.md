- = seznam
- jednoduchá datová struktura obsahující předem neznámý počet prvků
- data v uzlech (= nodes)
	- uzel obsahuje také ukazatel na následující uzel ([[Linked list|linked list]]), nebo i na předchozí uzel ([[Double linked list|double linked list]])
- rychlé a snadné přidání a odebrání prvků
	- paměť alokována při každém přidání, uvolněna při každém odebrání

<br>

- časová složitost
	- přidání: $O(1)$
	- hledání: $O(n)$ - drahé!
	- přístup na i-tý prvek: $O(i) = O(n)$ - drahé! Nepoužívat když je takový přístup nutný, to je práce pro (příp. dynamická) pole!

<br>

- v Python nestandardní, dostupné v knihovnách

#B3B33ALP
