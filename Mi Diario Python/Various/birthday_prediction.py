# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 17:01:13 2022

@author: Bryan
"""

year = int(input('Enter the preset year: '))

c = 0
name = [0]*3
birthday = [0]*3

while c < 3:
    name[c] = input('Enter your name: ')
    birthday[c] = int(input('Enter your birthday year: '))
    c += 1

for i in range(3):
    y_aged = year - birthday[i]
    print(f'{name[i]} is {y_aged}, this year.')

    