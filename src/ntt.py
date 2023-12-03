
import numpy as np 

def ntt(a : np.array, w : int, q : int, barret_reduction = False) -> np.array:  
    
    N     = len(a) 
    n_vec = np.linspace(0, N-1, N) 
    a_hat = np.zeros(N)
 
    for k in range(N):   
        w_vec     = np.mod(np.power(w*np.ones(N), k*n_vec), q*np.ones(N)) 
        a_hat[k]  = np.sum(np.multiply(w_vec, a)) % q  

    return a_hat 

def intt(a_hat : np.array, w : int, q : int, barret_reduction = False) -> np.array:  
    
    N     = len(a_hat)
    N_inv = (N**(q - 2)) % q 
    n_vec = np.linspace(0, N-1, N) 
    a     = np.zeros(N)
 
    for k in range(N):   
        w_vec     = np.mod(np.power(w*np.ones(N), k*n_vec), q*np.ones(N)) 
        w_vec_inv = np.mod(np.power(w_vec, (q-2)*np.ones(N)))
        a[k]      = N_inv * np.sum(np.multiply(w_vec_inv, a_hat)) % q  

    return a 

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