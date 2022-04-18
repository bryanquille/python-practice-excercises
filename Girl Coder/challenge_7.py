# Evaluate a formula

def main():

    D = input('Enter values separated by commas: ')
    D = D.split(',')
    for d in D:
        d = float(d)
        Q = ((2*50*d)/30)**(1/2)
        Q = round(Q, 2)
        if str(int(d)) != D[-1]:
            print(Q,end=', ')
        else:
            print(Q,end='')
    
if __name__ == '__main__':
    main()