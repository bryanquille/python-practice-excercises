# Find the future value
# We have the next data:
# The current money (c)
# The interes rate (x)
# The year of inversion (n)

def main():

    moneda = input('Ingrese la moneda a usar: ')
    c = float(input('Ingrese el valor actual: '))
    x = float(input('Ingrese la tasa de interes en % (0-100): '))
    n = float(input('Ingrese el número de años a aplicarse el interes: '))

    f_v = c * ((1+(x/100))**n)
    print(f'El valor futuro será de: {round(f_v, 2)} {moneda}.')


if __name__ == '__main__':
    main()