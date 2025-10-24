# -*- coding: utf-8 -*-
"""
Try to guess the secret number!
This code will let you know if you're too high, too low or right on the spot :)'
"""
secret = 6
guess = int(input("What's your guess? : "))
if (secret == guess):
    print("You guessed it!")
elif (secret < guess):
    print("You guessed too high!")
else :
    print("You guessed too low!")

