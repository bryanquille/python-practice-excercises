# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 19:37:09 2022

@author: Bryan
"""

def filter_str(l, n):
    
    j = 0
    c = 0
    
    # Here, we find the quantity of strings with more than n characters.
    for i in l:
        if len(i) > n:
            j += 1
    
    ln = list(range(j))
    
    # Here, we add the strings with more than n characters on a list.
    for k in l:
        if len(k) > n:
            ln[c] = k
            c += 1
            
    # Here, we verify if there is a string with more than n characters.
    if len(ln) == 0:
        print('There is any string with that amount of characters.')
    else:
        return ln    