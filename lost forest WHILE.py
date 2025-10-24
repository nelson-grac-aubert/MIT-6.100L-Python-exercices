# -*- coding: utf-8 -*-
"""
you are in the lost forest and need to escape!
"""

where = input("Are you going left or right? ")
while (where != 'left'):
    print('it seems like youre going in circles...')
    where=input("Are you going left or right? ")
print('You have escaped the lost forest!')
