# Este es el juego Master Mind
import random
from tracemalloc import stop

def main():
    
    l_c = int(input("Longitud de la cadena (Entre 2 y 9): "))
    if l_c < 2 or l_c > 9:
        print('La longitud debe ser entre 2 y 9.')
    else:
        i_n = 10 ** (l_c-1)
        f_n = '9'*l_c
        #print(i_n)
        #print(f_n)
        num = str(random.randint(i_n, int(f_n)))
        print(num)
    
        num_ad = '0'*l_c
        #c = 0

        while num_ad != num:

            c = 0
            if num_ad == '0'*l_c:
                num_ad = input("Adivina el número: ")
                if len(num_ad) != l_c:
                    print('La longitud de la cadena de números es incorrecta.')
                    break
            else:        
                for i in range(len(num)):
                    if num_ad[i] == num[i]:
                        c +=1
                print(f"Con {num_ad} has adivinado {c} valores.")
                num_ad = input("Adivina el número: ")
                if len(num_ad) != l_c:
                    print('La longitud de la cadena de números es incorrecta.')
                    break

        if num_ad == num:
            print(f"Con {num_ad} has adivinado {l_c} valores.")
            print("Felicitaciones adivinaste el número.")


if __name__ == "__main__":
    main()
