# write a code that loops a for loop over some range, and prints how many EVEN
# numbers are in that range : (5)(10)(2,9,3)(-4,6,2)(5,6)

numberofeven = 0
for step in range(5,6):
    if (step/2 == int(step/2)):
        numberofeven += 1
print('this range has',  numberofeven,  'even numbers')    

# AUTRE METHODE UTILISANT % reste après division


even_num = 0
for i in range (10):
    if i%2==0:
        even_num += 1
print('the second range has',  even_num,  'even numbers')