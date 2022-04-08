"""
Escribe una función que lea las palabras de un archivo de texto (texto.txt) y construya una lista donde cada palabra es un elemento de la lista.
"""
def main():
    with open('archivo.txt') as archivo:
        list_0 = []
        for contenido in archivo:
            list_0.append(contenido)
        # print(list_0)
    
    conc = ''
    for i in range(len(list_0)):
        # print(list_0[i].find('\n'))
        list_0[i] = list_0[i].replace('\n',' ')
        conc = conc + list_0[i]
    # print(list_0)
    # print(conc)

    list_1 = conc.split(sep=' ')
    print(list_1)


if __name__ == '__main__':
    main()