"""
Este programa muestra primero el listado de categorías de películas y pide al usuario que introduzca el código de la categoría de la película y posterior a ello pide que el usuario introduzca el número de días de atraso, y así se muestra al final el total a pagar.
"""

def peliculas_intro():

    print('CATEGORÍA             PRECIO        CÓDIGO        RECARGO/DÍA DE RETRASO')
    print('Favoritos             $2.50            1                  $0.50         ')
    print('Nuevos                $3.00            2                  $0.75         ')
    print('Estrenos              $3.50            3                  $1.00         ')
    print('Super Estrenos        $4.00            4                  $1.50         ')

def main():
    
    peliculas_intro()

    # Precio películas
    pp = {'Favoritos':2.50, 'Nuevos':3.00, 'Estrenos':3.50, 'Super Estrenos':4.00}  

    # Código películas
    cp = {'1':'Favoritos', '2':'Nuevos', '3':'Estrenos', '4':'Super Estrenos'}  

    # Recargo por día de retraso
    rp = {'1':0.50, '2':0.75, '3':1.00, '4':1.50}

    cd = input('Introduzca el código de la categoría de la película: ')
    dr = int(input('Introduzca el número de días de retraso en la devolución: '))

    print(f'El total a pagar es ${(pp[cp[cd]])+(dr*rp[cd])}')


if __name__ == '__main__':
    main()
