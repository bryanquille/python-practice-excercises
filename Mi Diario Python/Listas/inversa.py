"""
Escribe una función llamada "inversa" que busque todas las palabras inversas de una lista.
Ejemplo de palabras inversas: radar, oro, rajar, rallar, salas, somos, etc...
"""
def palindromo(str):
    
    inv_str = ""
    for letra in str:
        inv_str = letra + inv_str
    
    if str == inv_str:
        return True
    else:
        return False

def inversa():
    
    list_0 = ['radar', 'oro', 'avión', 'rajar', 'escuela', 'rallar', 'amigos', 'salas', 'somos', 'patín', 'bob', 'teatro', 'ana', 'leon', 'sometemos', 'seres']
    print('Las palabras inversas son: ')
    for i in list_0:
        if palindromo(i):
            print(i)
    

if __name__ == '__main__':
    inversa()