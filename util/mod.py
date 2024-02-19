
def sum_vec_mod(vec, q): 
    summation = 0 
    for i in range(len(vec)): 
        summation = (summation + vec[i]) % q 
    return summation 

def invert_vec_mod(vec, q):
    inv_vec = [ pow(vec[i], -1, q) for i in range(len(vec)) ]
    return inv_vec 