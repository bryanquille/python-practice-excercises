"""
Escribe una función "ordenada" que tome una lista como parámetro y devuelva True si la lista está ordenada en orden ascendente y devuelva False en caso contrario.
Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada([b, a]) retorna False.
"""

def ordenada(list_1):

    list_2 = list(list_1)
    list_1.sort()
    
    if list_1 == list_2:
        print(True)
        return True
    else:
        print(False)
        return False

def main():
    
    list_1 = [1, 2, 3, 4]
    list_2 = ['b', 'a']
    list_3 = ['a', 'b', 'c']
    ordenada(list_1)
    ordenada(list_2)
    ordenada(list_3)

if __name__ == '__main__':
    main()