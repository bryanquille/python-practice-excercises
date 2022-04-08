"""
De la galería de productos, el usuario introducirá el código y el número de unidades del producto que desea comprar. El programa determinará el total a pagar, como una factura.
Una variante a este ejercicio que lo haría un poco más complejo sería dar la posibilidad de seguir ingresando diferentes códigos de productos con sus respectivas cantidades, y cuando el usuario desee terminar el cálculo de la factura completa con todas sus compras.
"""

def main():

    prod = {
            '1':'Camisa',
            '2':'Cinturón',
            '3':'Zapatos',
            '4':'Pantalón',
            '5':'Calcetines',
            '6':'Falda',
            '7':'Gorra',
            '8':'Sueter',
            '9':'Corbata',
            '10':'Chaqueta'
           }
    
    precio = {
              'Camisa':25,
              'Cinturón':20,
              'Zapatos':60,
              'Pantalón':45,
              'Calcetines':5,
              'Falda': 20,
              'Gorra':10,
              'Sueter':30,
              'Corbata':10,
              'Chaqueta':80
             }
    
    print('PRODUCTO........CÓDIGO........PRECIO')
    print("Camisa............1.............25")
    print("Cinturón..........2.............20")
    print("Zapatos...........3.............60")
    print("Pantalón..........4.............45")
    print("Calcetines........5.............05")
    print("Falda.............6.............20")
    print("Gorra.............7.............10")
    print("Sueter............8.............30")
    print("Corbata...........9.............10")
    print("Chaqueta..........10............80")

    ne = 'si'  # Nueva entrada
    c = 0

    while ne == 'si' or ne == 's':

        pe = int(input("Elija un producto, introduzca el código: "))  # Producto escogido
        if pe <= 0 or pe > 10:
            print("Introduzca un código de la tabla.")
            ne = input('Desea ingresar otro producto? ')
        else:
            for cd in prod:
                if str(pe) == cd:
                    print(f'El precio de {prod[cd]} es ${precio[prod[cd]]}')
                    cant = int(input("Introduzca el número de unidades: "))
                    c = c + cant*precio[prod[cd]]

            ne = input('Desea ingresar otro producto? ')

        if ne == 's' or ne == 'si':
            continue
        else:
            print(f'El total a pagar es ${c}')
            


if __name__ == "__main__":
    main()