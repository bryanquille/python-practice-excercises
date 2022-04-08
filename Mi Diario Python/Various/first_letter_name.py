# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 17:53:56 2022

@author: Bryan
"""

names = ['Bryan', 'Daren', 'Juana', 'Maritza', 'Isaac', 'Veronica', 'Angelica', 'Francisco', 'Rosa', 'Patricio', 'Alexander']

letter = input('Enter a letter: ')
l = len(names)
c = 0

for i in range(l):
    if names[i][0] == letter:
        c += 1
print(c)
        