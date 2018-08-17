from math import floor
from functools import reduce


def calculate_expected_value(sumArray, lValue, rValue):
    sumValue = sumArray[rValue] - sumArray[lValue-1]
    length = rValue - lValue + 1
    return sumValue//length


def main():
    arrayLength, noOfQueries = list(map(int, input().strip().split(' ')))
    array = list(map(int, input().strip().split(' ')))
    queries = []
    sumArray = [0] * (arrayLength+1)
    for iterator in range(1, arrayLength+1):
        sumArray[iterator] = sumArray[iterator-1]+array[iterator-1]
    for iterator in range(noOfQueries):
        lrArray = list(map(int, input().strip().split(' ')))
        queries.append({'lValue': lrArray[0], 'rValue': lrArray[1]})
    for iterator in range(noOfQueries):
        print(calculate_expected_value(sumArray,
                                       queries[iterator]['lValue'], queries[iterator]['rValue']))


if __name__ == '__main__':
    main()
