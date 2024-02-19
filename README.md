# NTT PY

Python Implementation of the Number Theoretic Transform (NTT), developed with [numpy](https://numpy.org/). NTT PY supports both the cyclic form and negacylic form of the transform. 

# Usage: 
Ensure all prerequisies are satisfied (`pip install -r requirements.txt`). 

## Cyclic Transform 
Use `ntt` for the forward transform: 

```python
>>> import numpy as np
>>> from src.ntt import ntt, intt
>>> q = 11; w = 3;
>>> a_hat = ntt(np.array([7, 8, 3, 4, 10]), w, q)
>>> print(a_hat)
[10.  8. 10.  8. 10.]
```

and `intt` for the backwards transform: 

```python
>>> a = intt(a_hat, w, q)
>>> print(a)
[ 7.  8.  3.  4. 10.]
```

## Negacyclic Transform
Use `ntt_n` for the forward transform and `intt` for the backward transform. 

# NTT Background   
## Cyclic Form 

Given the finite field $`\mathbb{Z}_q`$ , for $`q > 1`$ prime, and a primitive $N$ th root of unity over $`\mathbb{Z}_q`$, $`\omega \in \mathbb{Z}_q`$, the NTT is the map 
$`\textbf{NTT}: \mathbb{Z}_q^N \rightarrow \mathbb{Z}_q^N `$ which sends $`(a_0, a_1, ... , a_{N-1})`$ to $`(\hat{a}_0, \hat{a}_1, ... , \hat{a}_{N-1})`$ using the rule:   

```math 
\hat{a}_k := \sum_{n=0}^{N-1} a_n \omega^{nk} \mod{q} $$
```

for $`0 \leq k < N`$: such is the cyclic form of the transform. Indeed, the vector $`(a_0, a_1, ... , a_{N-1})`$ is identified with the coefficients of the $`\mathbb{Z}_q`$ valued polynomial $`a_0 + a_1 x + \dotsm + a_{N-1} x^{N-1}`$ in the quotient ring $`\mathbb{Z}_q[x] / \langle x^N - 1 \rangle `$. In this light, the NTT in its cyclic form computes the following ring isomorphism: 

```math
\mathbb{Z}_q[x] / \langle x^N - 1 \rangle \cong \prod_{k=0}^{N-1} \mathbb{Z}_q[x] / \langle x - \omega^k \rangle 
```

which is an expression of the Chinese Remainder Theorem. Note that in the product ring, multiplication is point-wise. Thus, one can easily perform multiplication in $`\mathbb{Z}_q[X]`$, modulo $`x^N - 1`$, as follows:  

```math
\textbf{NTT}^{-1}\{ \textbf{NTT}\{a\} \cdot \textbf{NTT}\{b\}\}
```

where $`\cdot`$ is meant to denote the dot product and $`\textbf{NTT}^{-1}`$ is the inverse NTT, defined by: 

```math 
a_n = N^{-1} \sum_{k=0}^{N-1} \hat{a}_k \omega^{-nk} \mod{q} $$
```

## Negacyclic Form 
Here, we require some $`\psi \in \mathbb{Z}_q`$ such that $`\psi^2 = \omega`$. That is, $`\psi`$ is a $`2N`$ th root of unity over $`\mathbb{Z}_q`$. We hence send $`(a_0, a_1, ... , a_{N-1})`$ to $`(\hat{a}_0, \hat{a}_1, ... , \hat{a}_{N-1})`$ using the rule: 

```math 
\hat{a}_k := \sum_{n=0}^{N-1} a_n \psi^{(2k + 1)n} \mod{q} 
```
for $`0 \leq k < N`$: such is the negacyclic form of the transform. Identifying vectors with polynomials in $`\mathbb{Z}_q[x] / \langle x^N + 1 \rangle `$, the NTT in negacyclic form computes the ring isomorphism: 

```math
\mathbb{Z}_q[x] / \langle x^N + 1 \rangle \cong \prod_{k=0}^{N-1} \mathbb{Z}_q[x] / \langle x - \psi^{2k + 1} \rangle 
```

Note that here, the inverse transform is: 

```math 
a_n = N^{-1} \sum_{k=0}^{N-1} \hat{a}_k \psi^{-(2k + 1)n} \mod{q}
```

