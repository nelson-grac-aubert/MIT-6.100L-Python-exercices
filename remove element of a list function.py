def remove_element(L, e) : 
    """
    L is a list
    Returns a new list with elements in the same order as L 
    but without any elements equal to e 
    """

    newlist = []
    for element in L :
        if element != e :
            newlist.append(element)
    
    return newlist

L = [1,2,2,2]
print(remove_element(L,2))

Lili = [1,2,3,4,2,5,2,6]
print(remove_element(Lili, 2))

