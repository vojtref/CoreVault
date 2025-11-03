- $y = f(x)$ - funkční hodnota funkce $f$ v bodě $x$
- $A = D(f)$ - definiční obor funkce $f$
	- $D(f) \subseteq \R$
- $H(f)$ - obor hodnot funkce $f$ (příp. $R(x)$ z angl. "range")
	- $H(f) \subseteq \R$
	- $H(f) = \{y \in \R, \forall{x \in D(f)}:y=f(x)\}$
- $f: D(f) \to H(f)$ - zobrazení z definičního oboru na obor hodnot
- př.
	- $D(g) = A_1 \subset A_2 = D(f),\ f(x) = g(x)\ \forall x \in D(g)$
		- $g$ - zůžení funkce $f$
		- $f$ - rozšíření funkce $g$
- $\sgn x = \begin{cases}-1 & x<0 \\ 0 & x=0 \\ 1 & x>0\end{cases}$
	- signum (znaménko)

- operace s funkcemi

|                      |      $h$      |       $h(x)$        |                      $D(h)$                      |
| :------------------- | :-----------: | :-----------------: | :----------------------------------------------: |
| součet               |    $f + g$    |    $f(x) + g(x)$    |                 $D(f) \cap D(g)$                 |
| rozdíl               |    $f - g$    |    $f(x) - g(x)$    |                 $D(f) \cap D(g)$                 |
| součin               |  $f \cdot g$  |  $f(x) \cdot g(x)$  |                 $D(f) \cap D(g)$                 |
| podíl                | $\frac{f}{g}$ | $\frac{f(x)}{g(x)}$ | $(D(f) \cap D(g)) \setminus \{x \mid g(x) = 0\}$ |
| násobek ($a \in \R)$ |  $a \cdot f$  |   $a \cdot f(x)$    |                      $D(f)$                      |
- vlastnosti funkcí
	- prostá funkce
		- $f(x_1) = f(x_2) \implies x_1 = x_2$
	- inverzní funkce
		- $f_{-1}(x) = y \iff f(y) = x$
		- $f_{-1}(f(x)) = x$
	- sudá funkce
		- $\forall{x \in D(f)}: f(x) = f(-x)$
	- lichá funkce
		- $\forall{x \in D(f)}: f(x) = -f(-x)$ resp. $-f(x)=f(-x)$
	- periodická funkce
		- $\forall{x \in D(f)},p>0:f(x)=f(x + p)$
		- $p$ musí být nezávislá na $x$! Závislé $p$ $\implies$ $f$ není periodická
	- spojitá funkce
		- $x_0 \in D(f)$
		- $\forall{U(f(x_0))}\exists{U(x_0)}:(\forall x \in {U(x_0) \cap D(f)} : f(x) \in U(f(x)))$
- určování def. oboru
	- $f(x)^{g(x)}=e^{g(x) \ln f(x)}$ - výrazně usnadňuje práci
