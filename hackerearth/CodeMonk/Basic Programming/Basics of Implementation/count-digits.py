def count_digits(number):
    dictA = {}
    for iterator in range(10):
        dictA[iterator] = number.count(str(iterator))
    for iterator in range(10):
        print(iterator, dictA[iterator])


def main():
    number = input().strip()
    count_digits(number)


if __name__ == '__main__':
    main()
