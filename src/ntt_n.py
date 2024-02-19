
import numpy as np 

from util.exp import reduce_exponents, exponentiate_vec_mod
from util.mod import invert_vec_mod, sum_vec_mod 

'''
Computes the negacyclic form of the NTT.  
    a: ndarray, shape (n,)
        numpy array of length N, with entries in the finite field Z_q for q prime
    psi: int 
        Positive integer corresponding to primitive 2Nth root of unity over Z_q, i.e psi^2N ~ 1 mod q 
    q: int 
        Positive prime integer denoting the order of the finite field, Z_q 
'''
def ntt_n(a : np.ndarray, psi : int, q : int, barret_reduction = False) -> np.ndarray:

    N     = len(a) 
    n_vec = np.linspace(0, N-1, N) 
    a_hat = np.zeros(N) 

    for k in range(N): 

        exp_vec  = reduce_exponents((2*k + 1)*n_vec, 2*N)
        psi_vec  = psi*np.ones(N)
        psi_vec  = exponentiate_vec_mod(list(psi_vec), list(exp_vec), q) 

        prod_vec = [(a[n] * psi_vec[n]) % q for n in range(N)]
        a_hat[k] = sum_vec_mod(prod_vec, q) % q 

    return a_hat 

'''
Computes the cyclic form of the inverse NTT. 
    a_hat: ndarray, shape (n,)
        numpy array of length N, with entries in the finite field Z_q for q prime
    psi: int 
        Positive integer corresponding to primitive 2Nth root of unity over Z_q, i.e psi^2N ~ 1 mod q 
    q: int 
        Positive prime integer denoting the order of the finite field, Z_q 
'''
def intt_n(a_hat : np.ndarray, psi : int, q : int, barret_reduction = False) -> np.ndarray:

    N     = len(a_hat)
    N_inv = (N**(q - 2)) % q
    
    k_vec = np.linspace(0, N-1, N) 
    a     = np.zeros(N)

    for n in range(N):

        exp_vec = reduce_exponents(n*(2*k_vec + 1), 2*N) 
        psi_vec = psi*np.ones(N)

        psi_vec     = exponentiate_vec_mod(list(psi_vec), list(exp_vec), q) 
        psi_vec_inv = invert_vec_mod(psi_vec, q)   

        prod_vec = [ (a_hat[k] * psi_vec_inv[k]) % q for k in range(N) ]  
        a[n]     = N_inv * sum_vec_mod(prod_vec, q) % q 

    return a 

# For validation purposes: sufficient for small N
def slow_ntt_n(a : list, psi : int, q : int, barret_reduction = False) -> list:

    N     = len(a)
    a_hat = [0]*N 

    for k in range(N): 
        sum = 0 
        for n in range(N):
            psi_exp = (psi**(n*(2*k + 1))) % q 
            sum     = (sum + (a[n]*psi_exp % q)) % q
        a_hat[k] = sum 

    return a_hat

# For validation purposes: sufficient for small N 
def slow_intt_n(a_hat : list, psi : int, q : int, barret_reduction = False) -> list:
    
    N     = len(a_hat)
    N_inv = (N**(q - 2)) % q  
    a     = [0]*N 

    for n in range(N): 
        sum = 0 
        for k in range(N): 
            psi_exp     = (psi**(n*(2*k + 1))) % q 
            psi_exp_inv = (psi_exp**(q - 2)) % q 
            sum         = (sum + ((a_hat[k]*psi_exp_inv) % q)) % q   
        a[n] = (N_inv * sum) % q

    return a  