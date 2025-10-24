def remove_all(L,e) : 
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e 
    Return None
    """
    Lcopy = L[:]
    L.clear()

    for i in Lcopy : 
        if i != e : 
            L.append(i)
    return L 

Liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
remove_all(Liste,20)
print(Liste)

def remove_these(L,e) : 
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e 
    Return None
    """
    while e in L : 
        L.remove(e)

Listeb = [100, 200, 300, 200, 100, 500, 600, 400, 800, 500, 400]
remove_all(Listeb,200)
print(Listeb)