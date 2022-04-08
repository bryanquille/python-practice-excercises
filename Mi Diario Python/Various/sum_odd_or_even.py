# Identificar si la suma de los dígitos de un numero es par o impar.

def main():

    number = input("Enter an integer number (>=10): ")

    if number.isnumeric() and int(number) >= 10:
        s_d = 0
        for i in number:
            s_d = s_d + int(i)
        if s_d % 2 == 0:
            print(f'The sum of digits on {number} is {s_d} and is even.')
        else:
            print(f'The sum of digits on {number} is {s_d} and is odd.')
    else:
        print('The input value is wrong.')

if __name__ == '__main__':
    main()