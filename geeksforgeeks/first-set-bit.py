def find_first_set_bit(number):
    numberInBinary = '{0:b}'.format(number)
    for index, digit in enumerate(numberInBinary[::-1]):
        if digit == '1':
            return index + 1
    return 0


def main():
    print('First set bit', find_first_set_bit(6))


if __name__ == '__main__':
    main()
