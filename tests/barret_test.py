
import sys 
import time 
import bcolors as b 
import random as rand 

from util.barret import Barret 

def barret_test(q): 

    barret_unit = Barret(q) 

    a = int(rand.uniform(q, 1000*q)) 

    print(f"Modulus:         {q}")
    print(f"Input to Reduce: {a}")  

    t0 = time.perf_counter() 
    a_prime_modulo_op = a % q 
    t1 = time.perf_counter()

    t2 = time.perf_counter() 
    a_prime_barret_red = barret_unit.reduce(a) 
    t3 = time.perf_counter() 

    t4 = time.perf_counter() 
    a_prime_barret_red_bit = barret_unit.reduce_bit_shifts(a) 
    t5 = time.perf_counter() 

    print("===========================================================")
    print(f"Input Reduced (Mod. Operator):         {a_prime_modulo_op}")
    print(f"Input Reduced (barret.reduce):         {a_prime_barret_red}")
    print(f"Input Reduced (barret.reduce_bitwise): {a_prime_barret_red_bit}")
    print("===========================================================")
    print(f"Execution Time (Mod. Operator) [us]:         {1_000_000*(t1 - t0)}")
    print(f"Exectuion Time (barret.reduce) [us]:         {1_000_000*(t3 - t2)}")
    print(f"Execution Time (barret.reduce_bitwise) [us]: {1_000_000*(t5 - t4)}")
    print("===========================================================")

    res1 = ""
    res2 = "" 

    color1 = None 
    color2 = None 

    if(a_prime_modulo_op == a_prime_barret_red): 
        res1   = "PASS"
        color1 = b.PASS 
    else: 
        res1   = "FAIL" 
        color1 = b.FAIL  

    if(a_prime_modulo_op == a_prime_barret_red_bit):
        res2   = "PASS"
        color2 = b.PASS
    else: 
        res2   = "FAIL"
        color2 = b.FAIL

    print("Test Results:")
    print(color1 + "Test #1 (barret.reduce):         " + res1 + b.ENDC) 
    print(color2 + "Test #2 (barret.reduce_bitwise): " + res2 + b.ENDC) 
    return 

if __name__ == "__main__": 

    q = 8380417 

    print("Launching Barret test...")
    barret_test(q)

    print("Exiting Barret test...")
    sys.exit() 