def sort_sen(sen) :
    """
    sen is a string representing a sentence
    Returns a list containing all the words in sen sorted in alphabetical order
    """

    list = sen.split()
    list.sort()
    return list

print(sort_sen("look at this photograph"))
