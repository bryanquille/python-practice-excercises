# Sort alphabetically

def main():

    data = input('Enter some words separated by commas: ')
    data = data.replace(" ", "")
    data_list = data.split(',')
    data_list.sort()
    data = ', '.join(data_list)
    print(data)

if __name__ == '__main__':
    main()