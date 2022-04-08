# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 17:43:14 2022

@author: Bryan
"""

def leap_year(year):
    
    if year % 4 == 0 and year % 100 != 0:
        print('The year {year} is leap.')
    else:
        print("The year is not leap.")
        
if __name__ == '__main__':
    year = int(input("Enter a year: "))
    leap_year(year)