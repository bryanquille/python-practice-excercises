# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 19:03:30 2022

@author: Bryan
"""

def most_large_str(lstr):
    
    ln = [0]*len(lstr)
    j = 0
    c = 0
    x = False
    
    # Here, we find the lenght of the strings and add on a list ln
    for i in lstr:
        # print(len(i))
        # print(type(len(i)))
        ln[j] = len(i)
        j +=1
    # print(ln)
    
    # Here, we sort ln in order of decreasing
    while x == False:
        x = True
        for k in range(len(ln)-1):
            if ln[k] < ln[k+1]:
                n = ln[k]
                ln[k] = ln[k+1]
                ln[k+1] = n
                x = False
    p = ln[0]
    # print(p)
    # print(lstr)
    
    # Here, we find the position of the largest string
    for m in lstr:
        if len(m) == p:
            return lstr[c]
        else:
            c +=1    

    
 
        