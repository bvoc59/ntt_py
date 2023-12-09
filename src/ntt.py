
import numpy as np

from util.exp import reduce_exponents, exponentiate_vec_mod

'''
Computes the cyclic form of the NTT.  
    a: ndarray, shape (n,)
        numpy array of length N, with entries in the finite field Z_q for q prime
    w: int 
        Positive integer corresponding to primitive Nth root of unity over Z_q, i.e w^N ~ 1 mod q 
    q: int 
        Positive prime integer denoting the order of the finite field, Z_q 
'''
def ntt(a : np.ndarray, w : int, q : int, barret_reduction = False) -> np.ndarray:  
    
    N     = len(a) 
    n_vec = np.linspace(0, N-1, N) 
    a_hat = np.zeros(N)
    
    for k in range(N):   

        exp_vec  = reduce_exponents(k*n_vec, N)
        w_vec    = w*np.ones(N)
        w_vec    = exponentiate_vec_mod(list(w_vec), list(exp_vec), q)    

        a_hat[k] = np.sum(np.multiply(np.array(w_vec), a)) % q  
    
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
def intt(a_hat : np.ndarray, w : int, q : int, barret_reduction = False) -> np.ndarray:  
    
    N     = len(a_hat)
    N_inv = (N**(q - 2)) % q 
    k_vec = np.linspace(0, N-1, N) 
    a     = np.zeros(N)
    
    for n in range(N):   

        exp_vec     = reduce_exponents(n*k_vec, N) 
        w_vec       = w*np.ones(N)
        w_vec       = exponentiate_vec_mod(list(w_vec), list(exp_vec), q)    

        inv_exp_vec = reduce_exponents((q-2)*np.ones(N), N) 
        w_vec_inv   = exponentiate_vec_mod(list(w_vec), list(inv_exp_vec), q)
        
        a[n]        = N_inv * np.sum(np.multiply(np.array(w_vec_inv), a_hat)) % q  
    
    return a 

# For validation purposes only 
def slow_ntt(a : list, w : int, q : int, barret_reduction = False) -> list: 

    N     = len(a) 
    a_hat = [0]*N 
    
    for k in range(N): 
        sum = 0 
        for n in range(N): 
            w_exp  = (w**(n*k)) % q 
            sum    = (sum + (a[n]*w_exp % q)) % q   
        a_hat[k] = sum 

    return a_hat 

# For validation purposes only 
def slow_intt(a_hat : list, w : int, q : int, barret_reduction = False) -> list:  
    
    N     = len(a_hat)
    N_inv = (N**(q - 2)) % q 
    a     = [0]*N 

    for n in range(N): 
        sum = 0 
        for k in range(N): 
            w_exp     = (w**(n*k)) % q 
            w_exp_inv = (w_exp**(q - 2)) % q 
            sum       = (sum + ((a_hat[k]*w_exp_inv) % q)) % q   
        a[n] = (N_inv * sum) % q

    return a 

