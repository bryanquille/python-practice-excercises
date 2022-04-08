"""
Este programa pide primeramente la cantidad total de compras de una persona. Si la cantidad es inferior a $100.00, el programa dirá que el cliente no aplica a la promoción. Pero si la persona ingresa una cantidad en compras igual o superior a $100.00, el programa genera de forma aleatoria un número entero del cero al cinco. Cada número corresponderá a un color diferente de cinco colores de bolas que hay para determinar el descuento que el cliente recibirá como premio. Si la bola aleatoria es color blanco, no hay descuento, pero si es uno de los otros cuatro colores, sí se aplicará un descuento determinado según la tabla que  aparecerá, y ese descuento se aplicará sobre el total de compra que introdujo inicialmente el usuario, de manera que el programa mostrará un nuevo valor a pagar luego de haber aplicado el descuento.
"""
import random

def main():
    
    n = int(input("Introduzca la cantidad total de la compra: "))
    if n < 100:
        print('No aplica a la promoción')
    else:
        a = random.randint(0, 4)
        print("Su gasto iguala o supera los $100, por lo tanto participa en la promoción.")
        print("Color -> Descuento")
        print("Bola blanca -> 0", chr(37), "descuento")
        print("Bola roja -> 10", chr(37), "descuento")
        print("Bola azul -> 20", chr(37), "descuento")
        print("Bola verde -> 25", chr(37), "descuento")
        print("Bola amarilla -> 50", chr(37), "descuento")
        if a == 0:
            print("Aleatoriamente usted obtuvo una bola blanca.")
            print("Lamentablemente, no obtuvo descuento.")
            print(f"Su valor a pagar es ${n}")
        elif a == 1:
            print("Aleatoriamente usted obtuvo una bola roja.")
            print("Felicidades ha ganado un 10", chr(37), "de descuento.")
            print(f"Su valor a pagar es ${n-(n*0.1)}")
        elif a == 2:
            print("Aleatoriamente usted obtuvo una bola azul.")
            print("Felicidades ha ganado un 20", chr(37), "de descuento.")
            print(f"Su valor a pagar es ${n-(n*0.2)}")
        elif a == 3:
            print("Aleatoriamente usted obtuvo una bola azul.")
            print("Felicidades ha ganado un 25", chr(37), "de descuento.")
            print(f"Su valor a pagar es ${n-(n*0.25)}")
        elif a == 4:
            print("Aleatoriamente usted obtuvo una bola azul.")
            print("Felicidades ha ganado un 50", chr(37), "de descuento.")
            print(f"Su valor a pagar es ${n-(n*0.5)}")

if __name__ == "__main__":
    main()
