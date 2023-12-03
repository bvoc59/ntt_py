import sys

from tests.ntt_test import ntt_test

def z_97_n_16_ntt_test(): 

    q  = 97
    w  = 18  
    N  = 16
    
    ntt_test(q, w, N)
    return 

if __name__ == "__main__": 

    print("Launching NTT test...")
    z_97_n_16_ntt_test()   
    
    print("Exiting NTT test...")
    sys.exit() 