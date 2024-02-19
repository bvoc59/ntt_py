
import time 
import bcolors as b 
import numpy as np 

from src.ntt   import ntt, intt, slow_ntt, slow_intt 
from util.poly import gen_rand_poly 

'''
Simple NTT test framework. 
    q: int 
        Positive prime integer corresponding to the order of the 
        finite field with q elements, GF(q) ~ Z_q. 
    w: int 
        Positive integer corresponding to a primitive Nth root of 
        unity over Z_q, for some positive integer N. 
    N: int 
        Positive integer such that w^N ~ 1 mod q. 

The test framework consists of the following three tests. 

Test #1: 
Generate a random input polynomial with coefficients valued in Z_q. 
Take NTT using ntt() from src.ntt (test) and compare to NTT obtained from 
slow_ntt, also from src.ntt (validation). 

Test #2: 
Take NTT obtained from ntt() and apply intt() from src.ntt to obtain INTT (test)
and compare to INTT obtained with slow_intt, also from src.ntt (validation). 

Test #3: 
Test if INTT from intt() is equals original random polynomial. 
i.e Check that a = intt(ntt(a)). 
 
'''

def ntt_test(q, w, N): 

    print("NTT Parameters:") 
    print(f"q: {q}") 
    print(f"w: {w}")
    print(f"N: {N}")

    a = gen_rand_poly(N, q) 

    print("Random Input Polynomial:")
    print(a) 

    print("====================")
    print("Executing Test #1...")

    t0 = time.perf_counter() 
    a_hat = ntt(a, w, q) 
    t1 = time.perf_counter()  

    t2 = time.perf_counter() 
    a_hat_slow = slow_ntt(a, w, q)
    t3 = time.perf_counter()

    print("Test Output:") 
    print(a_hat) 

    print("Validation Output:")    
    print(a_hat_slow)

    result = ""
    color  = None 
    if((np.array(a_hat) == np.array(a_hat_slow)).all()):
        result = "PASS"
        color  = b.PASS 
    else:  
        result = "FAIL"
        color  = b.FAIL 

    print(color + "Test #1 Result: " + result + b.ENDC)
    print(f"Execution Time, ntt      [ms]: {1000*(t1 - t0)}")
    print(f"Execution Time, slow_ntt [ms]: {1000*(t3 - t2)}")

    if(result == "FAIL"):
        return 
    
    print("====================")
    print("Executing Test #2...")

    t0 = time.perf_counter() 
    a_inv = intt(a_hat, w, q) 
    t1 = time.perf_counter()  

    t2 = time.perf_counter() 
    a_inv_slow = slow_intt(a_hat, w, q)
    t3 = time.perf_counter()

    print("Test Output:") 
    print(a_inv) 

    print("Validation Output:")    
    print(a_inv_slow)

    if((np.array(a_inv) == np.array(a_inv_slow)).all()):
        result = "PASS"
        color  = b.PASS 
    else:  
        result = "FAIL"
        color  = b.FAIL 

    print(color + "Test #2 Result: " + result + b.ENDC)
    print(f"Execution Time, intt      [ms]: {1000*(t1 - t0)}")
    print(f"Execution Time, slow_intt [ms]: {1000*(t3 - t2)}")
    print("====================")

    print("Executing Test #3...")
    if((np.array(a_inv) == np.array(a)).all()):
        result = "PASS"
        color  = b.PASS 
    else:  
        result = "FAIL"
        color  = b.FAIL     

    print(color + "Test #3 Result: " + result + b.ENDC)
    return 

