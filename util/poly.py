
import random as rand 

'''
Generates a random polynomial of degree N-1, with entries in the finite 
field Z_q. 
    N: int
        Positive integer, corresponding to one more than degree of polynomial. 
    q: int
        Positive prime integer denoting order of the finite field, Z_q. 
'''
def gen_rand_poly(N, q): 
    poly = [0]*N 
    for n in range(N):
        poly[n] = int(rand.uniform(0, q-1))  
    return poly 


