"""
Escribir una función llamada "bisect" que tome una lista ordenada y una palabra como objetivo, y nos devuelva el índice en el que se encuentra en la lista, en caso de no aparecer en la lista devuelve "No se encontró la palabra".
"""

from bisect import *

def bisect_():
    vocales = ['a', 'e', 'i', 'o', 'u']
    x = input('Ingrese la posición de la vocal a encontrar: ')
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(vocales, x)
    if i != len(vocales) and vocales[i] == x:
        print(i)
        return i
    else:
        print('No se encontro.')

if __name__ == '__main__':
    bisect_()
    