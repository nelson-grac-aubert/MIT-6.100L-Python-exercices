def count_matches(d) : 
    """ d is a dictionnary
    returns how many entries in d have the key equals to its value """

    keyslist = list(d.keys())  # on récupère les clés dans une liste
    valueslist = list(d.values())  # on récupère les valeurs
    counter = 0 # on initialise un compteur

    for i in range (len(keyslist)) : # on itère sur la longueur des listes 
        if keyslist[i] == valueslist[i] : # si une clé est égale à sa valeur
            counter += 1 # le compteur augmente

    return counter

# for example
d = {1:2, 3:4, 5:6}
print(count_matches(d)) # returns 0 

d1 = {1:2, "a":"a", 5:5}
print(count_matches(d1)) # returns 2