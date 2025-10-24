def pairwise_div(Lnum, Ldenum) : 
    """ Lnum and Ldenum are non-empty lists of equal lenghts containing numbers 
    
    Returns a new list whose elements are the pairwise division of an element in Lnum by an element in Ldenum
    
    Raise a ValueError if Ldenum contains a 0 
    
    Raise an AssertionError if one of the lists doesn't meet its requirements """

    assert len(Lnum) == len(Ldenum) > 0, "Lists must be of equal size"
    assert len(Lnum) > 0 and len(Ldenum) > 0, "Lists cannot be empty" # releve une AssertError si la condition est remplie et affiche le message

    newlist = [] # on initialise une liste vide qui va contenir les résultats des divisions 

    for i in range(len(Lnum)) : # on itère sur la longueur des listes
        try : 
            division = Lnum[i] / Ldenum[i] # on essaie la division des index indentiques
            newlist.append(division) # on ajoute le résultat à la nouvelle liste

        except : # si une division n'est pas possibnle 
            raise ZeroDivisionError("Impossible de diviser par 0") # le programme crash, mais on choisit ce qu'il affiche

    return newlist

L1 = [4, 5, 6]
L2 = [1, 2, 3]

print(pairwise_div(L1, L2))

### réactiver les lignes suivantes pour faire crasher le programme et montrer la RaiseError 

# L3 = [4,5,6]
# L4 = [1,0,3]
# print(pairwise_div(L3, L4))     

##réactiver les lignes suivantes pour faire une AssertionError

# L5 = [4,5] 
# L6 = [1,0,3] 
# print(pairwise_div(L5, L6))  
        