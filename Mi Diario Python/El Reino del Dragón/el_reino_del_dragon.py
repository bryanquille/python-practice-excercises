#El Reino del Dragon....
import random
import time

def introduccion():
    print ("Estamos en una tierra llena de dragones. Delante de nuestro,")
    print ("se ven dos cuevas. En una cueva, el dragon es amigable")
    print ("y compartira el tesoro contigo. El otro dragon")
    print ("es codicioso y hambriento, y te va a comer ni bien te vea.")
    print ("")

def CambiarCueva():
    cueva = ""
    while cueva != "1" and cueva != "2":
        print ("Ha que cueva quieres entrar? 1 o 2?")
        cueva = input()
       
    return cueva

def cheqcueva(CambiarCueva):
    print ("Te acercas a la Cueva...")
    time.sleep(1)
    print ("Esta oscuro y tenebroso...")
    time.sleep(1)
    print ("Un gran dragon salta delante tuyo, abre su boca y...")
    print ("")
    time.sleep(1)
   
    FriendlyCueva = random.randint (1, 2)
   
    if CambiarCueva == str(FriendlyCueva):
        print("Te entrega el tesoro...")
        return "Te entrega el tesoro..."
    else:
        print("El dragon te come de un bocado....")
        return "El dragon te come de un bocado...."
   
EmpezarNuevo = ("si")
puntos = 0

while EmpezarNuevo == ("s") or EmpezarNuevo == ("si"):
    
    introduccion()

    NumCaverna = CambiarCueva()
        
    if cheqcueva(NumCaverna) == "Te entrega el tesoro...":
        puntos += 100
        print ("Quieres jugar de nuevo? (si o no)")
        EmpezarNuevo = input()

    else:
        print("Game over")
        print(f'Obtuviste {puntos} puntos')
        print ("Quieres jugar de nuevo? (si o no)")
        puntos = 0
        EmpezarNuevo = input()
    