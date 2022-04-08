"""
A - Escribe una función llamada "duplicado" que tome una lista y devuelva True si tiene algún elemento duplicado. La función no debe modificar la lista.
B - Crear una función que genere una lista de 23 números aleatorios del 1 al 100 y comprobar con la función anterior si existen elementos duplicados. (Puedes ver el módulo random como guía)
"""
import random

def duplicado(list_1):

    c = 0
    for i in range(len(list_1)):
        for j in range(len(list_1)):
            if i == j:
                continue
            elif list_1[i] == list_1[j]:
                c += 1
    if c != 0:
        print(True)

def main():

    list_1 = [0]*23
    for i in range(23):
        list_1[i] = random.randint(1, 100)
    print(list_1)
    duplicado(list_1)

if __name__ =='__main__':
    main()

