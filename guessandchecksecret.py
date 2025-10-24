secret = 34
x = 1

for i in range(1,11) :
    x += 1
    if i == secret :
        print("Found!")
    else :
        if x == 11 :
            print("Not Found!")