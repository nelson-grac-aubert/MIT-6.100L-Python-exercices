def find_in_L(Ld, k) : 
    """ Ld is a list of dictionnaries 
    k is an int 
    Returns True if k is a key in any dictionnaries of Ld and False otherwise """

    flag = False

    for dict in Ld : # on check chaque dictionnaire de la liste
        if k in dict : # si la clé existe dans le dictionnaire
            return True # break et retourne
        
    return False # si la clé n'est trouvée nulle part
    
# exemple 

d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}
print(find_in_L([d1, d2, d3], 2)) #returns True
print(find_in_L([d1, d2, d3], 25)) #returns False