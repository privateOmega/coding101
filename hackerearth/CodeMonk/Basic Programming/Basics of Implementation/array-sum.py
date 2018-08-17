def main():
    arrayLength = int(input())
    sum = 0
    array = list(map(int, input().strip().split(' ')))
    for iterator in range(arrayLength):
        sum += array[iterator]
    print(sum)


if __name__ == '__main__':
    main()
