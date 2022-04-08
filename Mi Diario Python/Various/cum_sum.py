"""
Escriba una función que tome una lista de números y devuelva la suma acumulada, es decir, una nueva lista donde el primer elemento es el mismo, el segundo elemento es la suma del primero con el segundo, el tercer elemento es la suma del resultado anterior con el siguiente elemento y así sucesivamente. Por ejemplo, la suma acumulada de [1,2,3] es [1, 3, 6].
"""

def main():

    list_1 = list(range(1, 11))
    list_2 = list(range(len(list_1)))

    sum_cum = 0
    for i in range(len(list_1)):
        list_2[i] = sum_cum + list_1[i]
        sum_cum = list_2[i]
    print(list_2)

    return list_2

if __name__ == "__main__":
    main()