
import math 
from ctypes import * 

class Barret(): 

    def __init__(self, q): 

        self.q     = q
        self.k     = math.ceil(math.log2(self.q)) 
        self.r_til = math.floor((4**self.k) / self.q)  

        self.q_fixed     = c_int64(self.q)  
        self.r_til_fixed = c_int64(self.r_til)
        return 
    
    def reduce(self, a_prime : int) -> int:

        t1 = math.floor((a_prime*self.r_til) / (4**self.k))  
        t2 = a_prime - t1*self.q 

        if(t2 >= self.q):
            t2 = t2 - self.q
        return t2     

    def reduce_bitwise(self, a_prime : int) -> int:  
        
        a_prime_fixed = c_int64(a_prime) 
        t1 = (self.r_til_fixed * a_prime_fixed) >> 46 
        t2 = a_prime_fixed - t1*self.q_fixed

        if(t2 >= self.q_fixed): 
            t2 = t2 - self.q_fixed
        return int(t2)  