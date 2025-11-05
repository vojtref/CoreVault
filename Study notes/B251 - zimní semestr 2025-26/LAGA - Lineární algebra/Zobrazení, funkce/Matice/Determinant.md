- Leibnizův vzorec $$\det \mathbf{A} = |\mathbf{A}| = \sum_{\pi \in S_n} \sign \pi \prod_{n=1}^{s} a_{\pi(n),n}$$
	- Velebil rozepsal ten součin po položkách, ale proč to dělat když to jde s dalším hieroglyfem
- zopakování: $S_n$ - množina všech permutací $n$-prvkové množiny
	- $\card S_n = n!$
	- př. $S_2$
		- $\mathbf{A} = \pmatrix{a_{11} & a_{12} \\ a_{21} & a_{22}}$
		- $\det \mathbf{A} = \begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{vmatrix}$
		- TODO: doplnit mapping $\pi$ atd
		- $\det \mathbf{A} = a_{11} \cdot a_{22} - a_{12} \cdot a_{21}$
	- př. $S_3$
		- TODO: doplnit, 3 věže
	- Sarrusovo pravidlo, snadný pattern dle hlavní a vedlejší diagonály neplatí pro $n \ge 4$
- TODO: doplnit rovnoběžníky v $\R^2$
- determinant počítá *orientovaný obsah* rovnoběžníku (resp. *orientovaný objem* rovnoběžnostěnu) se stranami ze sloupců matic
	- $P(\vec{e_1}, \vec{e_2}) = 1$
		- konvence
		- zavádí jednotku orientované plochy v $\R^2$
		- proti směru hodinových ručiček → +
- tvrzení: $\det \mathbf{A} = \det \mathbf{A}^T$
	- TODO: důkaz skrz komutativitu sčítání, a $\pi \to \pi^{-1}$ pouze přehodí pořadí (vše se stejně sečte)
- $\mathbf{A}$ je čtvercová matice v horním blokovém tvaru
	- $\mathbf{A} = \pmatrix{a_{11} \\ 0 & a_{22} \\ 0 & 0 & a_{33} \\ \vdots & \vdots & \vdots & \ddots \\ 0 & 0 & 0 & 0 & a_{nn}}$
	- $\therefore$
	- $\det \mathbf{A} = a_{11} \cdots a_{nn}$
		- všechny ostatní součiny jsou s min. jednou nulou, hlavní diagonála jediná možná nenulová
		- $a_{nn}$ může být i nulové, tudíž determinant i v horním blokovém tvaru může být = 0
- při počítání determinantu převedením do horního blokového tvaru skrz [[Gaussova eliminační metoda|GEM]] nutno kompenzovat elementární řádkové úpravy korekčními faktory danými před determinant (takřeč. **"opatrná" GEM**)
	- prohození řádků (prohození os) mění znaménko permutace (šroubujeme opačným směrem), nutno kompenzovat $-1$
		- mění znaménko orientovaného objemu
	- násobení řádků (= škálování os, změna měřítka) inverzním skalárem
		- roztáhnutí osy vynásobí objem, proto $\sim \; \ne \; =$
	- zkosení (přičtení násobku řádku) není nutno kompenzovat, zkosení plochu nemění
- jiný způsob: vnější mocniny $\ref{AKLA 5.2}$
	- moderní způsob
- TODO: doplnit Laplaceův rozvoj determinantu
- algebraický doplněk pozice $A_{i,j}$
- TODO: dopsat "rekurzivní" postup rozvoje dle sloupce $\ref{AKLA 8.3.4}$
	- výhodné v případě že zvolený sloupec obsahuje jednu či více nul, není nutno počítat příslušný algebraický doplněk
- strukturální vlastnosti $\det \mathbf{A}$ o rozměrech $n \times n$
	- $\det \mathbf{E}_n = 1$
	- $\det (\mathbf{B} \cdot \mathbf{A}) = \det \mathbf{B} \cdot \det \mathbf{A}$
		- TODO: doplnit neformální "důkaz" z foto
		- $\R^2 \xrightarrow{\mathbf{A}} \R^2 \xrightarrow{\mathbf{B}} \R^2$
	- pro isomorfismus $\mathbf{A}$: $\det(\mathbf{A}^{-1}) = (\det \mathbf{A})^{-1}$
	- $\det(a \cdot \mathbf{A}) = a^n \cdot \mathbf{A}$
		- vynásobení každé hrany daného rovnoběžnostěnu
- př.

$$
\array{
	\mathbf{A} = \pmatrix{2 & 7 \\ 5 & 3} \\\\
	\text{matice alg. doplňků pozic v A} \\
	\pmatrix{A_{1,1} & A_{1,2} \\ A_{2,1} & A_{2,2}} \\
	\begin{array}{l}
		A_{1,1} = \left|\matrix{1 & 7 \\ 0 & 3}\right| = 3 \\
		A_{1,2} = \left|\matrix{2 & 1 \\ 5 & 0}\right| = -5 \\
		A_{2,1} = \left|\matrix{0 & 7 \\ 1 & 3}\right| = -7 \\
		A_{2,2} = \left|\matrix{2 & 0 \\ 5 & 1}\right| = 2 \\
	\end{array} \\
	\text{adjugovaná matice } \mathop{\mathrm{adj}} \mathbf{A} = \pmatrix{A_{1,1} & A_{1,2} \\ A_{2,1} & A_{2,2}}^T = \pmatrix{3 & -7 \\ -5 & 2}\\\\
	
	\mathbf{A} \cdot \mathop{\mathrm{adj}} \mathbf{A} = \pmatrix{2 & 7 \\ 5 & 3} \cdot \pmatrix{3 & -7 \\ -5 & 2} = \pmatrix{-29 & 0 \\ 0 & -29} = (-29) \cdot \pmatrix{1 & 0 \\ 0 & 1}\\
	\mathop{\mathrm{adj}} \mathbf{A} \cdot \mathbf{A} = \pmatrix{3 & -7 \\ -5 & 2} \cdot \pmatrix{2 & 7 \\ 5 & 3} = \pmatrix{-29 & 0 \\ 0 & -29} = (-29) \cdot \pmatrix{1 & 0 \\ 0 & 1}
}
$$

- Cramerova věta pro isomorfismus $\mathbf{A}$
	- $\mathbf{A} \cdot \adj \mathbf{A} = \det{\mathbf{A}} \cdot \mathbf{E}_n = \adj \mathbf{A} \cdot \mathbf{A}$
	- $\therefore$ inverze $\mathbf{A}^{-1} = (\det \mathbf{A})^{-1} \cdot \adj \mathbf{A}$