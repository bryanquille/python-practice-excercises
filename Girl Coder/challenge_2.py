from numpy import number


# Calculate the factorial of a given number

def main():

    try:
        n = int(input('Enter a number: '))
        l = list(range(1, n+1))
        f = 1
        for i in l:
            f = f * i
            if i < n:
                print(f'{i} x ', end='')
            else:
                print(f'{i} ', end='')
        print(f'= {f}')
    except ValueError:
        print('The input value is wrong.')

if __name__ == '__main__':
    main()