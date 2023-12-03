
import sys 
import time
import bcolors as b 
import numpy as np 

from src.ntt   import ntt, intt 
from util.poly import gen_rand_poly 

'''
NTT performance test over the finite field of order 8380417, Z_8380417, with
1753 our N = 512th root of unity, since 1753^512 ~ 1 mod 8380417. 
'''

def z_8380417_n_512_test(): 

    q = 8380417
    w = 1753
    N = 512 

    print("NTT Parameters:") 
    print(f"q: {q}") 
    print(f"w: {w}")
    print(f"N: {N}")

    a = gen_rand_poly(N, q)

    print("Applying NTT to random input sequence...")
    t0 = time.perf_counter() 
    a_hat = ntt(np.array(a), w, q)
    t1 = time.perf_counter()    

    print(f"Execution Time, ntt [ms]: {1000*(t1 - t0)}")

    '''
    print("Applying inverse NTT to output sequence...") 
    t0 = time.perf_counter() 
    a_out = intt(a_hat, w, q)
    t1 = time.perf_counter()    

    print(f"Execution Time, intt [ms]: {1000*(t1 - t0)}")

    result = ""
    color  = None 
    if((np.array(a_out) == np.array(a)).all()):
        result = "PASS"
        color  = b.PASS 
    else:  
        result = "FAIL"
        color  = b.FAIL 

    print(color + "Test Result: " + result + b.ENDC)
    '''
    return 

if __name__ == "__main__": 
    
    print("Launching NTT test...")
    z_8380417_n_512_test()   

    print("Exiting NTT test...")
    sys.exit() 