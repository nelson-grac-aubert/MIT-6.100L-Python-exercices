def in_list_of_lists(L,e) :
    """ L is a list whose elements are lists containing ints
    Return true is e is an element within the lists of L 
    False otherwise """

    if len(L) == 0 :
            return False
    
    else : 
        if e in L[0] : 
            return True
        else :
            return in_list_of_lists(L[1:],e)

test = [[1,2], [3,4], [9, 8, 7]]
print(in_list_of_lists(test, 0))
print(in_list_of_lists(test, 9))