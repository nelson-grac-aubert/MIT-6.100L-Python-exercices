def char_count(s) :
    """
    s is a string of lowercase chars 
    Return a tuple where the first element is the amount of wovels in s and 
    the second element is the amount of consonants in s 
    """
    countvowels = 0
    countconsonnants = 0
    for letter in s : 
        if letter in "aeiouy" : 
            countvowels += 1
        else : 
            countconsonnants += 1 
    return (countvowels, countconsonnants)

print(char_count("ffffgplmnt"))
print(char_count("aaaeeeiiiooouu"))
print(char_count("bababababababa"))
print(char_count(""))