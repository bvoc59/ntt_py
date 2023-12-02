## NTT PY

Python Implementation of the Number Theoretic Transform (NTT). 

## NTT Background   

Given the finite field $`\mathbb{Z}_q`$ , for $`q > 0`$ prime, and an $N$ th root of unity over $`\mathbb{Z}_q$, $\omega \in \mathbb{Z}_q`$, the NTT is the map 
$`\textbf{NTT}: \mathbb{Z}_q^N \rightarrow \mathbb{Z}_q^N `$ which sends $`(a_0, a_1, ... , a_{N-1})`$ to $`(\hat{a}_0, \hat{a}_1, ... , \hat{a}_{N-1})`$ using the rule:   

```math 
\hat{a}_k := \sum_{n=0}^{N-1} a_n \omega^{nk} \mod{q} $$
```

for $`0 \leq k < N`$. Indeed, the vector $`(a_0, a_1, ... , a_{N-1})`$ is identified with the coefficients of the $`\mathbb{Z}_q`$ valued polynomial $`a_0 + a_1 x + \dotsm + a_{N-1} x^{N-1} \in \mathbb{Z}_q[x]`$. In this light, the NTT computes the following ring isomorphism: 

```math
\mathbb{Z}_q[x] / \langle x^N - 1 \rangle \cong \prod_{k=0}^{N-1} \mathbb{Z}_q[x] / \langle x - \omega^k \rangle 
```

which is an expression of the Chinese Remainder Theorem. Note that in the product ring, multiplication is point-wise. Thus, one can easily perform multiplication in $`\mathbb{Z}_q`$, modulo $`x^N - 1`$ as follows:  

```math
\textbf{NTT}^{-1}\{ \textbf{NTT}\{a\} \cdot \textbf{NTT}\{b\}\}
```

where $`\cdot`$ is meant to denote the dot product and $`\textbf{NTT}^{-1}`$ is the inverse NTT. 