# dark forest but after 2 wrong paths, it adds a sad smiley face

n = 0
answer = input('which way are you going? right or left? ')
while (answer != 'left') :
    n = n+1
    if (n>2) :
        print('youre going in circles... :(')
        answer = input('which way are you going? right or left? ')
    else :
        print('youre going in circles')
        answer = input('which way are you going? right or left? ')
else :
    print('you got out of the forest!')
    



