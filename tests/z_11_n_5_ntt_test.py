
import sys

from tests.ntt_test import ntt_test

'''
usage: python -m tests.z_11_n_5_ntt_test
'''

def z_11_n_5_ntt_test(): 

    q  = 11
    w  = 3  
    N  = 5
    
    ntt_test(q, w, N)
    return 

if __name__ == "__main__": 

    print("Launching NTT test...")
    z_11_n_5_ntt_test()   
    
    print("Exiting NTT test...")
    sys.exit(0) 