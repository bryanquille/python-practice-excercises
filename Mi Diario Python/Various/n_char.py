# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 12:13:34 2022

@author: Bryan
"""

def n_char(n, x):
    
    if type(x) == str:
        return x*n
    else:
        print('The second value must be a character')