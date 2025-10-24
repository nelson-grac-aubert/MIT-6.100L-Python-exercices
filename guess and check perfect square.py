x = int(input("What number do you want to check? " ))
guess = 0 
negflag = False
if x < 0 :
    negflag = True
while guess**2 < x :
    guess += 1
if guess**2 == x :
    print("square root of", x, "is", guess)
else :
    print(x, "is not a perfect square")
    if negflag :
        print("Just checking, did you mean", -x, "?")