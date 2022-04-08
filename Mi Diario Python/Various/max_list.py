# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 16:13:41 2022

@author: Bryan
"""

# def max_list(list_1):
    
#     nlist = sorted(list_1, reverse=True)
#     #print(nlist)
#     return nlist[0]

def max_in_list(l):
    
    x = False
    while x == False:
        x = True
        for i in range(len(l)-1):
            if l[i] < l[i+1]:
                n = l[i]
                l[i] = l[i+1]
                l[i+1] = n
                x = False
    return l[0]                