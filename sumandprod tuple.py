def sum_and_prod(L) :
    """
    input L is a list of numbers
    Return a tuple where the first element is sum of all elements in L 
    the second element of the tuple is the product of all elements in L 
    """
    sum = 0 
    product = 1  

    for element in L : 
        sum += element
        product = product * element

    return (sum, product)

print(sum_and_prod([1,1,1,1]))
print(sum_and_prod([2,4,-6]))
print(sum_and_prod([45,2]))