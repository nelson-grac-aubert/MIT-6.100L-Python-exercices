def make_ordered_list(n) : 
    """
    n is a positive integer
    return a list containing all ints in order from 0 to n (inclusive)
    
    """
    result = []
    for chiffre in range(0,n+1) : 
        result.append(chiffre)
    
    return result 

print(make_ordered_list(2))
print(make_ordered_list(12))
print(make_ordered_list(4))
