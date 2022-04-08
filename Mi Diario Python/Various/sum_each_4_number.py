"""
Para un numero N menor de 100. Mostrar la suma 
de los cuadrados de los números que están separados 
entre si cuatro posiciones.
"""

def main():

    number = input("Enter a number between 1 - 100: ")
    if number.isnumeric():
        l_n = list(range(1, int(number)+1))
        c = 0
        sum_4 = 0
        for i in l_n:
            if c <= int(number)-1:
                sum_4 = sum_4 + l_n[c]
                # print(sum_4)
                c += 4
                # print(c)
            else:
                break
                
        print(f'The sum is {sum_4}.')


if __name__ == "__main__":
    main()