# Rhyme words

def main():

    w1 = input('Escriba la primera palabra: ')
    w2 = input('Escriba la segunda palabra: ')
    
    if w1[-3] == w2[-3] and w1[-2] == w2[-2] and w1[-1] == w2[-1]:
        print('Las palabras riman.')
    elif w1[-2] == w2[-2] and w1[-1] == w2[-1]:
        print('Las palabras rima un poco.')
    else:
        print('Las palabras no riman.')


if __name__ == '__main__':
    main()