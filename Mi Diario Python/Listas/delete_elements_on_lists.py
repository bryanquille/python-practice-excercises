"""
Escribe una función llamada "elimina" que tome una lista y elimine el primer y último elemento de la lista y cree una nueva lista con los elementos que no fueron eliminados.
Luego escribe una función que se llame "media" que tome una lista y devuelva una nueva lista que contenga todos los elementos de la lista anterior menos el primero y el último.
"""

def elimina(list_1):

    list_1.pop(0)
    list_1.pop()

def media(list_2):

    list_2.pop(0)
    list_2.pop()

def main():

    # Creating a list
    l = input("Enter the lenght of the list: ")
    if l.isnumeric():
        list_1 = [0] * (int(l)+1)
        for i in range(0, int(l)+1):
            list_1[i] = input(f"Enter the {i} value of the list: ")
        print(list_1)
        elimina(list_1)
        media(list_1)
        print(list_1)
    else:
        print("The input value is wrong.")

if __name__ == '__main__':
    main()