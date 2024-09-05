# Universes
 > (Universe) $U$: finite set

$U = \{0, 1\}^n$ ($\{0, 1\}^2 = \{ 00, 01, 10, 11 \}$)

> ***Def:*** **Probability distribution** $P$ over $U$ is a function $P: U \longrightarrow [0, 1]$ (weights or the probability of the element in the universe) such that $\sum_{x \in U}P(x) = 1$

> $|U|$ - size of the universe (number of the elements)

Examples:
1. *Uniform distribution*: $\forall x \in U: P(x) = 1/|U|$\
2. *Point distribution* at $x_0$ : $P(x_0) = 1, \forall x \neq x_0: P(x) = 0$ 
m
> Distribution vector: $(P(000), P(001), ...P(111))$ 

# Events
> - For a set $A \subseteq U$ : $Pr[A] = \sum_{x \in A} P(x) \in [0, 1]$
> - The set A is called an **event**

*Note: $Pr[U] = 1$*
Example: $U = \{0, 1\}^8$ ($|U| = 256$)
	A = $\{$ all $x$ in $U$ such that $lsb_2(x)=11 \} \subseteq U$
	for the uniform distribution on $\{0, 1\}^8: Pr[A] = 1/4$
# The union bound
> For events $A_1$ and $A_2 \subseteq U$ 
	$Pr[A_1 \cup A_2]\le Pr[A] + Pr[B]$

$A_1 \cap A_2 = \emptyset \Rightarrow Pr(A_1 \cup A_2) = Pr[A_1] + Pr[A_2]$

Example:
	$A_1 = \{\forall x \in \{0, 1\}^n \mid lsb_2(x) = 11\}$
	$A_2 = \{\forall x \in \{0, 1\}^n \mid msb_2(x)=11\}$
	$Pr[lsb_2(x) = 11 \vee  msb_2(x)=11] = Pr[A_1 \cup A_2] \le \frac{1}{4} + \frac{1}{4} = \frac{1}{2}$

# Random variables
> ***Def*** : a **random variable** $X$ is a function $X: U \longrightarrow V$ 

Example: $X: \{0, 1\}^n \rightarrow \{0, 1\}$; $X(y) = lsb(y) \in \{0, 1\}$ 
For the uniform distribution on $U$:
	$Pr[X=0] = \frac{1}{2}, Pr[X=1]=\frac{1}{2}$
> Random variable $X$ induces a distribution on $V: Pr[X=v] := Pr[X^{-1}(v)]$

## The uniform random variable
> Let $U$ be some set, e.g. $U = \{0, 1\}^n$
> We write $r \xleftarrow{R} U$ to denote a **uniform random variable** over U
> 	for all $a \in U: Pr[r=a] = \frac{1}{|U|}$
> (formally, $r$ is the identity function: $r(x) = x \forall x \in U$)

# Randomised algorithms
- Deterministic algorithm: 
	  $y \longleftarrow A(m)$ 
- Randomized algorithm
	  $y \longleftarrow A(m; r)$ where $r \xleftarrow{R} \{0, 1\}^n$ 
	output is a random variable $y \xleftarrow{R} A(m)$ 
	![[Pasted image 20240905205218.png]]
# Independence
>***Def:*** events $A$ and $B$ are **independent** if $Pr[A \land B] = Pr[A] \cdot Pr[B]$

Random variabkles $X, Y$ taking values in $V$ are **independent** if $\forall a, b \in V: Pr[X=a] \land Y=b] = Pr[X=a] \cdot Pr[Y=b]$

# XOR
XOR of two strings in $\{0, 1\}^n$ is their bit-wise addition mod 2

| $x$ | $y$ | $x\oplus y$ |
| --- | --- | ----------- |
| 0   | 0   | 0           |
| 1   | 0   | 1           |
| 0   | 1   | 1           |
| 1   | 1   | 0           |
Example: $011011 \oplus 1011010 = 1101101$

>***Thm:*** $Y$ a random variable over $\{0, 1\}^n$, $X$ an independent uniform variable on $\{0, 1\}^n$
	Then $Z:=Y \oplus X$ is uniform variable on $\{0, 1\}^n$.

***Proof:*** (for $n=1$)

| Y   | $Pr[Y]$ | X   | $Pr[X]$       |
| --- | ------- | --- | ------------- |
| 0   | $p_0$   | 0   | $\frac{1}{2}$ |
| 1   | $p_1$   | 1   | $\frac{1}{2}$ |

| Y   | X   | $Pr$            |
| --- | --- | --------------- |
| 0   | 0   | $\frac{p_0}{2}$ |
| 0   | 1   | $\frac{p_0}{2}$ |
| 1   | 0   | $\frac{p_1}{2}$ |
| 1   | 1   | $\frac{p_1}{2}$ |

$$
Pr[Z=0] = 
$$
$$
= Pr[(X, Y) = (0, 0) \wedge (X, Y) = (1, 1)] =
$$
$$
= Pr[(X, Y) = (0, 0)] + Pr[(X, Y) = (1, 1)] =
$$
$$
= \frac{p_0}{2} + \frac{p_1}{2} = (p_0 + p_1) \cdot \frac{1}{2} =\frac{1}{2}
$$
## The birthday paradox
> Let $r_1, ..., r_2 \in U$ be independent identically distributed random variables
> ***Thm:*** when $n = 1.2 \cdot \sqrt{|U|}$ then $Pr[\exists i\neq j : r_i = r_j] \ge \frac{1}{2}$

Exampe: Let $U=\{0, 1\}^{128}$, $|U| = 2^128$
	After sampling about $2^{64}$ random messages from $U$, some two sampled messages will likely be the same.
$1.24 \cdot \sqrt{365} \approx 24$ people