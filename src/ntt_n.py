
import numpy as np 

from util.exp import reduce_exponents, exponentiate_vec_mod 

'''
Computes the negacyclic form of the NTT.  
    a: ndarray, shape (n,)
        numpy array of length N, with entries in the finite field Z_q for q prime
    w: int 
        Positive integer corresponding to primitive Nth root of unity over Z_q, i.e w^N ~ 1 mod q 
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

        a_hat[k] = np.sum(np.multiply(np.array(psi_vec), a)) % q   

    return a_hat 

'''
Computes the cyclic form of the inverse NTT. 
    a_hat: ndarray, shape (n,)
        numpy array of length N, with entries in the finite field Z_q for q prime
    w: int 
        Positive integer corresponding to primitive Nth root of unity over Z_q, i.e w^N ~ 1 mod q 
    q: int 
        Positive prime integer denoting the order of the finite field, Z_q 
'''
def intt_n(a_hat : np.ndarray, psi : int, q : int, barret_reduction = False) -> np.ndarray:

    N     = len(a_hat)
    N_inv = (N**(q - 2)) % q
    
    k_vec = np.linspace(0, N-1, N) 
    a     = np.zeros(N) 

    for n in range(N):

        exp_vec     = reduce_exponents((2*n + 1)*k_vec, 2*N)
        exp_vec_inv = exponentiate_vec_mod(list(exp_vec), list((q - 2)*np.ones(N)), q)
        
        psi_vec     = psi*np.ones(N)
        psi_vec     = exponentiate_vec_mod(list(psi_vec), list(exp_vec_inv), q)

        a[n]        = (N_inv * np.sum(np.multiply(np.array(psi_vec), a_hat))) % q   

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