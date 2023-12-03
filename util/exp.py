
import numpy as np 

'''
Reduce the elements of an exponent vector modulo N. 
    exp_vec: list 
        List corresponding to vector of exponents. 
    N: int 
        Positive prime integer corresponding to factor to 
        reduce by. 
'''
def reduce_exponents(exp_vec : np.array, N : int) -> np.array:
    i = 0 
    for exp in exp_vec: 
        if(exp == N):
            exp_vec[i] = 0     
        elif(exp > N): 
            exp_vec[i] = exp_vec[i] % N 
        else:
            pass 
        i = i + 1 
    return exp_vec  

'''
Raise the elements of input vector to the elements of exponent vector and store 
result modulo q. 
    in_vec: list
        List of integers corresponding to input vector. 
    exp_vec: list
        List of positive integers corresponding to exponents. 
    q: int 
        Positive integer to reduce values by.
'''
def exponentiate_vec_mod(in_vec : list, exp_vec : list, q : int) -> list:       
    out_vec = [0]*len(in_vec)
    for i in range(len(in_vec)):
        out_vec[i] = int(in_vec[i]) ** int(exp_vec[i]) 
        out_vec[i] = out_vec[i] % q
    return out_vec