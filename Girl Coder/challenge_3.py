# The sequence of data separated by comma, transform to a list and a tuple

def main():

    seq = input('Enter a sequence separated by coma: ')
    seq_list = seq.split(',')
    seq_tuple = tuple(seq_list)
    print(seq_list)
    print(seq_tuple)

if __name__ == '__main__':
    main()