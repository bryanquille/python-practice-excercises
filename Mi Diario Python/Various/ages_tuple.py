# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 17:25:39 2022

@author: Bryan
"""
a = 0
c = 0
age = [0]*10

while c < 10:
    
    age[c] = int(input('Enter an age: '))
    c += 1

ages = tuple(age)

for i in ages:
    if i > 20:
        a += 1

print('\n')
print(f'{a} people are greater than 20.')