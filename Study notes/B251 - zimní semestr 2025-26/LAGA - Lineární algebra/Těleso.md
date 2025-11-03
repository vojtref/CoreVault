- obecně $\F$, anglicky "skew field" či "division ring"
- trojice množiny tzv. skalárů, operace $+: \F^2 \to \F$, a operace $\cdot: \F^2 \to \F$ s danými vlastnostmi
	- vlastnosti $+$
		- existence nulového prvku neutrálního vzhledem ke sčítání
		- komutativita
		- asociativita
		- existence opačného skaláru
	- vlastnosti $\cdot$
		- existence jednotky neutrální vzhledem k násobení
		- komutativita
		- asociativita
	- distributivní zákon
	- **test invertibility**: $\forall a \in \F: a \ne 0 \iff a^{-1} \in \F$
		- $a^{-1}$ tzv. inverzní prvek: $a \cdot a^{-1} = 1$
		- rozlišuje těleso od okruhu (odtud angl. název "division ring")
- př. množina zbytků po dělení $m$ neboli $Z_m$ (viz modulární aritmetika)
	- $Z_m = \{n \in \Z:n \lt m\} = \{0, 1, \ldots, m-1\}$
	- $Z_2, Z_3, Z_5, \ldots$
	- pozor! těleso tvoří pouze pokud $m$ je prvočíslo (tj. pouze $Z_p$ tvoří tělesa), viz Fermatova malá věta
		- v opačném případě soudělnost dělitele a prvků v množině, např. $Z_6$ nesplňuje test invertibility ($2^{-1} \notin Z_6$)

- $Z_5$:

| $+$    |  0  |  1  |  2  |  3  |  4  |
| :----- | :-: | :-: | :-: | :-: | :-: |
| **0**  |  0  |  1  |  2  |  3  |  4  |
| **1**  |  1  |  2  |  3  |  4  |  0  |
| **2**  |  2  |  3  |  4  |  0  |  1  |
| **3**  |  3  |  4  |  0  |  1  |  2  |
| **4**  |  4  |  0  |  1  |  2  |  3  |


| $\cdot$ |  0  |  1  |  2  |  3  |  4  |
| :----- | :-: | :-: | :-: | :-: | :-: |
| **0**  |  0  |  0  |  0  |  0  |  0  |
| **1**  |  0  |  1  |  2  |  3  |  4  |
| **2**  |  0  |  2  |  4  |  1  |  3  |
| **3**  |  0  |  3  |  1  |  4  |  2  |
| **4**  |  0  |  4  |  3  |  2  |  1  |
