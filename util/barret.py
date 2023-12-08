
import math 

class Barret(): 

    def __init__(self, q): 

        self.q     = q
        self.k     = math.ceil(math.log2(self.q)) 
        self.r_til = math.floor((4**self.k) / self.q)  
        self.shift = 2*self.k 

        return 
    
    def reduce(self, a_prime : int) -> int:

        t1 = math.floor((a_prime*self.r_til) / (4**self.k))  
        t2 = a_prime - t1*self.q 

        return t2 if (t2 < self.q) else (t2 - self.q) 

    def reduce_bit_shifts(self, a_prime : int) -> int:  
        
        t1 = (self.r_til * a_prime) >> self.shift 
        t2 = a_prime - t1*self.q

        return t2 if (t2 < self.q) else (t2 - self.q)