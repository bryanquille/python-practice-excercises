# Find the numbers between 2000 and 3200 which are divisible by 7, but not multiples of 5.

def main():

    numbers = list(range(2000, 3201))
    d7_n5 = []
    for i in numbers:
        if i%7 == 0 and i%5 != 0:
            d7_n5.append(i)
    print(d7_n5)        

if __name__ == '__main__':
    main()