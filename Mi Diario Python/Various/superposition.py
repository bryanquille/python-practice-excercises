"""
Created on Tue Feb 22 11:59:28 2022

@author: Bryan
"""

def superposition(list1, list2):
    
    for i in list1:
        for j in list2:
            if i == j:
                return True

