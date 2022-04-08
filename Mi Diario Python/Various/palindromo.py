# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:34:17 2022

@author: Bryan
"""

def palindromo(str):
    
    inv_str = ""
    for letra in str:
        inv_str = letra + inv_str
    
    if str == inv_str:
        return True
    else:
        return False
            