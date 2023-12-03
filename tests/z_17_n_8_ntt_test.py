import sys

from tests.ntt_test import ntt_test

def z_17_n_8_ntt_test(): 

    q  = 17
    w  = 8  
    N  = 8
    
    ntt_test(q, w, N)
    return 

if __name__ == "__main__": 

    print("Launching NTT test...")
    z_17_n_8_ntt_test()   
    
    print("Exiting NTT test...")
    sys.exit() 