"""
Los números de las claves de dos cajas fuertes están mezcladas en un
número entero llamado clave maestra. Determine ambas claves, la primera
clave se construye con los dígitos impares de la clave maestra y la
segunda con los pares. Ejemplo: Clave Maestra= 12345, clave1=135,
clave2=24.
"""

def main():

    clave_maestra = input("Enter an integer number: ")
    if clave_maestra.isnumeric():
        clave1 = ''
        clave2 = ''
        for i in clave_maestra:
            if int(i) % 2 == 0:
                clave2 = clave2 + i
            else:
                clave1 = clave1 + i

        print(f'Clave1: {clave1}')
        print(f'Clave2: {clave2}')
    else:
        print("The input value is wrong.")

if __name__ == '__main__':
    main()