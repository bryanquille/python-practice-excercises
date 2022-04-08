"""
Escribe una función llamada "elimina_duplicados" que tome una lista y devuelva una nueva lista con los elementos únicos de la lista original. No tienen porque estar en el mismo orden.
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
                
    
def elimina_duplicados():

    list_1 = []
    for i in range(23):
        list_1.append(random.randint(1, 100))
    print(list_1)
    duplicado(list_1)
    list_2 = list(set(list_1))
    duplicado(list_2)
    print(list_2)

if __name__ == '__main__':
    elimina_duplicados()