def print_numbers():
    with open('numbers.txt') as file:

        string=file.readline()
        for numbers in string:
            if numbers != ',':
                print(numbers,end='')
            else: print()


if __name__=='__main__':
    print_numbers()