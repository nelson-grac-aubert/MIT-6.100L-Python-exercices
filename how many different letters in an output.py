# Assume you are given a string of lowercase letters in variable s
# Count how many unique letters there are in the string
# for example s = abca : the answer is 3 

s = input('Give a word to check for different characters : ')
dif_char = ''
for letter in s:
    if letter not in dif_char:
        dif_char = dif_char + letter
print (len(dif_char))