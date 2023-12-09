
import numpy as np 

from util.exp import reduce_exponents, exponentiate_vec_mod 


'''
Computes the 


'''
def ntt_n():
    return

def intt_n(): 
    return 

# For validation purposes only 
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

# For validation purposes only 
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