# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 20:18:39 2022

@author: Bryan
"""

rstr = input('Enter a string: ')

c = 0

for i in rstr:
    if i.isupper():
        c +=1

if c != 0:
    print(f'The string has {c} upper case characters.')
else:
    print('The string has no upper case characters.')