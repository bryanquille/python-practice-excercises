# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 20:42:35 2022

@author: Bryan
"""

def bin_to_int(b):
    
    # Resources
    le = len(b)
    l = sorted(list(range(le)),reverse=True)
    bn = [0]*le
    
    # print(bn)
    
    c = 0    # Counter
    
    # I convert each 1 or 0 to an integer and add them on a list
    for i in b:
        bn[c] = int(i)
        c += 1
    
    # print(bn)
    # print(l)
    
    
    # I use a formula for get an integer from a binary number
    integer = [0]*le
    for j in range(le):
        integer[j] = bn[j]*2**l[j]
    
    # print(integer)
    
    # I sum the list obtained with the formula
    c1 = 0
    for k in integer:
        s = c1 + k
        c1 = s
        
    return s     # I get the integer number from the binary number
    
    
    