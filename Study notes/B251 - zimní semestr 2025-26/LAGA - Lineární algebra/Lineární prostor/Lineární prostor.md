- lineární prostor $\L$ nad obecným [[Těleso|tělesem]] $\F$
- prvky v $\L$ tzv. vektory, $+: \L^2 \to \L$ (sčítání vektorů), a $\cdot: \F \times \L \to \L$ (škálování/násobení vektorů skalárem), splňující dané axiomy:
	- vlastnosti $+$
		- existence nulového vektoru $\vec{o}$ neutrálního vzhledem ke sčítání: $\vec{x} + \vec{o} = \vec{x}$
		- komutativita: $\vec{a} + \vec{b} = \vec{b} + \vec{a}$
		- asociativita: $(\vec{a} + \vec{b}) + \vec{c} = \vec{a} + (\vec{b} + \vec{c})$
		- existence opačného vektoru: pro každé $\vec{x}$ existuje právě jedno $\vec{y}$, kde platí $\vec{x} + \vec{y} = \vec{o}$
	- vlastnosti $\cdot$
		- neutralita $1$ vzhledem ke škálování: $1 \cdot \vec{x} = \vec{x}$
		- asociativita: $a \cdot (b \cdot \vec{x}) = (a \cdot b) \cdot \vec{x}$
	- distributivita
		- distributivita sčítání vektorů: $a \cdot (\vec{x} + \vec{y}) = a \cdot \vec{x} + a \cdot \vec{y}$
		- distributivita sčítání skalárů: $(a + b) \cdot \vec{x} = a \cdot \vec{x} + b \cdot \vec{x}$
- pro snadnější začátek příklady lineárních prostorů nad $\R$:
	- těleso $\R$ s příslušnými operacemi, dán lineární prostor $\L$ nad tělesem $\R$, prvky v $\L$ vektory, $+: \L^2 \to \L$ (sčítání vektorů), a $\cdot: \R \times \L \to \L$, obě operace splňující naše axiomy výše
	- $\R^n$
		- $n=2$
			- $\L = \R^2$
			- klasické vektory v rovině
			- např. $\pmatrix{3 \\ 4},\pmatrix{-2 \\ -1} \in \L$
			- ```desmos-graph
			  width=200; height=200;
			  bottom=-5; top=5;
			  left=-5; right=5;
			  ---
			  f(x)=4x/3|0<x<3|cyan
			  (3, 4)|cross|cyan
			  g(x)=x/2|-2<x<0|red
			  (-2, -1)|cross|red
			  ```
		- př. $n=5$
			- $\L = \R^5$
			- $\pmatrix{-1 \\ \sqrt{2} \\ 0 \\ 4 \\ 3} \in \R^5$
			- $\vec{x}=\begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5 \end{pmatrix}$
		- prvek v $\R^n$ možné znázornit nejen jako klasický vektor v $n$-dimenzionálním prostoru (v podstatě nemožné pro $n \geqslant 4$), ale i jako $n$-krát vzorkovaný signál $\viz{AKLA 1.1.8}$
	- $\R[x]$ - množina všech polynomů o neurčité $x$ s reálnými koeficienty
		- prvky např. $a(x) = \sqrt{2}x + 4$, $b(x) = 3x^2 - 4 + 5$...
		- platnost axiomů lineárního prostoru triviální dokázat
- dále např. $\Z_5[x]$ neboli množina polynomů o neurčité $x$ s koeficienty v $\Z_5$
- abychom nemuseli zkoumat prostory všechny jednotlivě nad každým jednotlivým tělesem, budeme je zkoumat všechny hromadně skrz vlastnosti které mají všechny společné