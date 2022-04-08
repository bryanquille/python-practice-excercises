# Para un número N imprimir su tabla de multiplicar.

def main():

    l_1_12 = list(range(1, 13))
    number = input("Enter a number: ")
    if number.isnumeric():
        print(f'Multiplication Table of {number}')
        for i in l_1_12:
            print(f'{number} x {i} = {int(number)*i}')
    else:
        print("The value you type is wrong.")

if __name__ == "__main__":
    main()