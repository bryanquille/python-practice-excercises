# Solicitar un número e imprimir los dígitos pares de este.

def main():
    number = input("Enter an integer number: ")
    if number.isnumeric():
        for i in number:
            if int(i) % 2 == 0:
                print(f'The digit {i} on {number} is even.')
    else:
        print("The input value is wrong.")

if __name__ == '__main__':
    main()