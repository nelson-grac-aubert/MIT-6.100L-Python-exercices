def count_words(sen) :
    """
    sen is a string representing a sentence
    Returns how many words are in sen (i.e words are sequences of characters separated by spaces " ")
    """
    phrase_splittée = sen.split()
    return len(phrase_splittée)

print(count_words("Bonjour je suis Nelson"))
print(count_words("a a a a a a a a a ailyena10"))