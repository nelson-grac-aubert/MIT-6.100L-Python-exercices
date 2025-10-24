def apply(criteria, n) :
    """
    criteria is a function that takes in a number and returns a bool
    n is an int

    Returns how many ints from 0 to n (inclusive) match the criteria (i.e returns True when run with the function criteria)
    """
    count = 0
    for i in range(0,n+1) : 
        if criteria(i) == True :
            count += 1
    return count

def is_even(a) :
    return a%2 == 0

def is_amultipleof3(a) :
    return a%3 == 0

evens = apply(is_even, 1000)
print(evens)

of3 = apply(is_amultipleof3, 1000)
print(of3)

print("apply with an anonymous function : ", apply(lambda x: x==8, 1000))

print((lambda x: x==8)(8))

