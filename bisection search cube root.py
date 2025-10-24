# write code to do a bisection search to find the cube root of positive cubes within
# some epsilon

cube = 34634636674536 
epsilon = 0.01
low = 0 
high = cube
guess = ((low + high)/2) 

while abs(cube - guess**3) > epsilon :
    guess = ((low + high)/2) 
    if guess**3 > cube :
        high = guess
    else :
        low = guess

print(f'An approximation of the square root of {cube} is {guess}')
