def square_list(liste) : 
    """
    square every element of a list, mutating it
    looping over the element index
    """

    for i in range(len(liste)) : 
        liste[i] = liste[i]**2 
    
    return liste # PAS BESOIN DE RETOURNER LA NOUVELLE LISTE : LES NOUVELLES VALEURS SONT ASSIGNEES, LA LISTE EST DEJA MODIFIEE

a = [1,2,3,4,5]

print(a)
square_list(a)
print(a)
square_list(a)
print(a)

def square_list2(liste) : 
    """
    square every element of a list, mutating it
    making a new variable representing the index and icnrementing it 
    """
    c = 0 
    while c < len(liste) :
        liste[c] = liste[c]**2
        c += 1 

    return liste

b = [2,4,6]

print(b)
square_list2(b)
print(b)
square_list2(b)
print(b)

def square_list3(liste) : 
    """
    square every element of a list, mutating it
    using the enumerate for i,e in enumerate(liste)
    """

    for i,valeur in enumerate(liste) :
        liste[i] = valeur**2 

    return liste

c = [3, 6, 9]

print(square_list3(c))
print(c)
print(square_list3(c))
print(c)
