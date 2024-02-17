import sys

from tests.ntt_test import ntt_test

'''
usage: python -m tests.z_137_n_34_ntt_test
'''
def z_137_n_34_ntt_test(): 

    q  = 137
    w  = 4 
    N  = 34 
    
    ntt_test(q, w, N)
    return 

if __name__ == "__main__": 

    print("Launching NTT test...")
    z_137_n_34_ntt_test()   
    
    print("Exiting NTT test...")
    sys.exit(0) 