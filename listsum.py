def list_sum(liste) :
    """
    input a list containing int or floats
    Returns the sum of the elements of that list
    """

    sum = 0 
    for i in liste : # i prends les valeurs des elements de la liste, dans l'ordre 
        sum += i
    return sum

print(list_sum([0,1,2,3]))
print(list_sum([56,44]))
print(list_sum([1,-1,2,-2]))
print(list_sum([1.5, -1.5, 2.2, 73/5]))

def len_sum(liste) : 
    """
    input a list containing strings
    Returns the sum of the lenghts of the string elements of that list 
    """

    longueur = 0 
    for string in liste : 
        longueur += len(string)
    return longueur 

print(len_sum(["u", "de", "tro", "quat"]))
print(len_sum(["aba", "bab"]))