# # Binary number divisible by 5


def main():

    b_n = input('Enter some binary numbers, separated by commas: ')
    b_n = b_n.replace(' ', '')
    b_n_list = b_n.split(',')
    b_l = []
    value = []
    for b in b_n_list:
        bn = '0b' + b
        b_l.append(bn)
        if int(bn, 2) % 5 == 0:
            value.append(bn)
    print(','.join(value))


if __name__ == '__main__':
    main()