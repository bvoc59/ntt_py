
import sys
import time 
import bcolors as b 
import numpy as np 

from src.ntt   import ntt, intt, slow_ntt 
from util.poly import gen_rand_poly 

'''
Simple NTT validation test over the finite field of order 11, Z_11, with 3 our N = 5th 
root of unity, since 3^5 ~ 1 mod 11.  

Tests ntt from src.ntt, with slow_ntt from src.ntt as validation. 
Then tests intt from src.ntt, applies to transformed sequence 
and tests if equals original sequence. 

'''

def z_11_n_5_ntt_test(): 

    q  = 11
    w  = 3  
    N  = 5

    print("NTT Parameters:") 
    print(f"q: {q}") 
    print(f"w: {w}")
    print(f"N: {N}")

    a  = gen_rand_poly(N, q) 

    print("In Sequence:")
    print(a) 

    t0 = time.perf_counter() 
    a_hat_slow = slow_ntt(a, w, q) 
    t1 = time.perf_counter() 

    t2 = time.perf_counter() 
    a_hat = ntt(np.array(a), w, q)
    t3 = time.perf_counter()

    print("Validation Out Sequence: slow_ntt")    
    print(a_hat_slow)

    print("Test Out Sequence: ntt") 
    print(a_hat) 

    result = ""
    color  = None 
    if((np.array(a_hat_slow) == np.array(a_hat)).all()):
        result = "PASS"
        color  = b.PASS 
    else:  
        result = "FAIL"
        color  = b.FAIL 

    print(color + "Test Result: " + result + b.ENDC)
    print(f"Execution Time, slow_ntt [ms]: {1000*(t1 - t0)}")
    print(f"Execution Time, ntt      [ms]: {1000*(t3 - t2)}")

    if(result == "FAIL"):
        return 

    print("Evaluating Inverse NTT...")

    t0 = time.perf_counter() 
    a_inv = intt(a_hat, w, q)
    t1 = time.perf_counter()

    print("Out Sequence: intt")
    print(a_inv) 

    if((np.array(a_inv) == np.array(a)).all()):
        result = "PASS"
        color  = b.PASS 
    else: 
        result = "FAIL"
        color  = b.FAIL 

    print(color + "Test Result: " + result + b.ENDC)
    print(f"Execution Time, intt     [ms]: {1000*(t1 - t0)}")
    return 

if __name__ == "__main__": 

    print("Launching NTT test...")
    z_11_n_5_ntt_test()   
    
    print("Exiting NTT test...")
    sys.exit() 