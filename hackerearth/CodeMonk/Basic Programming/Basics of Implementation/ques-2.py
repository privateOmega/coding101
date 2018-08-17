def main():
    arrayLength, rangeStart, rangeEnd = map(int, input().strip().split(' '))
    array = list(map(int, input().strip().split(' ')))
    status = True
    for iterator in array:
        if iterator not in list(range(rangeStart, rangeEnd + 1)):
            status = False
    if status:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
