def palindromeCount(list_a):
    count = 0
    for num in list_a:
        temp = num
        rev = 0
        while temp > 0:
            rev = rev * 10 + temp % 10
            temp = temp / 10
        if num == rev:
            count = count + 1
    print('Total number of palindromes in list', count)


def main():
    list_a = [10, 121, 133, 155, 141, 152]
    palindromeCount(list_a)


if __name__ == '__main__':
    main()
