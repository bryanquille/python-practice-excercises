# Determinar la cantidad de dígitos de un numero (1- 100000)

def main():

    number = input("Enter an integer between 1 - 100000: ")
    if number.isnumeric():
        if int(number) >=1 and int(number) <= 100000:
            c = 0
            for i in number:
                c += 1
            print(f"The number {number} has {c} digits.")
        else:
            print("The number must be between 1-100000.")
    else:
        print("The input argument is wrong.")

if __name__ == "__main__":
    main()