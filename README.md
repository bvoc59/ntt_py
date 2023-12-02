## NTT PY

Python Implementation of the Number Theoretic Transform (NTT), using the Radix-2, Cooley-Tukey Decimation-in-Time (DIT) Algorithm. 

## NTT Background   

Given the finite field $\mathbb{Z}_q$, for $q > 0$ prime, and an $N$ th root of unity over $\mathbb{Z}_q$, $\omega \in \mathbb{Z}_q$, the NTT is the map $\textbf{NTT}: \mathbb{Z}_q^N \rightarrow \mathbb{Z}_q^N$ which maps $(a_0, a_1, ... , a_{N-1})$ to $(\hat{a}_0, \hat{a}_1, ... , \hat{a}_{N-1})$ using the rule:   

$$ \hat{a}_k := \sum_{n = 0}^{N-1} a_n \omega^{nk} \mod{q} $$

for $0 \leq k < N$. 