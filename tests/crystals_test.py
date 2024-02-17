
import sys 
import time 
import bcolors as b 
import numpy as np 

from src.ntt_n  import ntt_n, intt_n
from util.poly import gen_rand_poly 

'''
CRYSTALS Dilithium NTT test. 
usage: python -m tests.crystals_test 
'''

def crystals_test(): 

    q   = 2**23 - 2**13 + 1 
    psi = 1753
    N   = 256

    print("NTT Parameters:") 
    print(f"q: {q}") 
    print(f"w: {psi}")
    print(f"N: {N}")

    a = gen_rand_poly(N, q) 

    print("====================")
    print("Executing Test #1...")

    t0 = time.perf_counter() 
    a_hat = ntt_n(a, psi, q) 
    t1 = time.perf_counter()  

    print(f"Execution Time, ntt_n [s]: {t1 - t0}")

    print("====================")
    print("Executing Test #2...")

    t0 = time.perf_counter() 
    a_inv = intt_n(a_hat, psi, q) 
    t1 = time.perf_counter()  

    print(f"Execution Time, intt_n [ms]: {t1 - t0}")
    
    print("====================")
    print("Executing Test #3...")
    if((np.array(a_inv) == np.array(a)).all()):
        result = "PASS"
        color  = b.PASS 
    else:  
        result = "FAIL"
        color  = b.FAIL     

    print(color + "Test #2 Result: " + result + b.ENDC)
    return 

if __name__ == "__main__":

    print("Launching Crystals Dilithium NTT test...")
    crystals_test()

    print("Exiting Crystals Dilithium NTT test...")
    sys.exit(0)