## NTT PY

Python Implementation of the Number Theoretic Transform, using the Radix-2, Cooley-Tukey Decimation-in-Time (DIT) Algorithm. 

Given the finite field $\mathbb{Z}_q$, for $q > 0$ prime, and an $N$ th root of unity over $\mathbb{Z}_q$, $\omega \in \mathbb{Z}_q$, the NTT is the map $\textbf{NTT}: \mathbb{Z}_q^N \rightarrow \mathbb{Z}_q^N$ defined as follows:  