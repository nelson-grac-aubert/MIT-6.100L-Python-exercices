def power_recur(n,p) : 
    """
    returns n**p using recursion
    """
    if p == 0 :
        return 1
    elif p == 1 : 
        return n 
    else :
        p = p-1
        return n * power_recur(n, p)
        

print(power_recur(5,3))
print(power_recur(5,2))   
print(power_recur(5,1))
print(power_recur(5,0))