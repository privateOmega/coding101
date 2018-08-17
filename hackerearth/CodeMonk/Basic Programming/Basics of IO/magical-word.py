from math import sqrt


def nearest_magical_char(target):
    primes = [67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
    left = 0
    right = len(primes) - 1
    while left < right:
        mid = (left + right) // 2
        if target < primes[mid]:
            right = mid
        elif target > primes[mid]:
            left = mid + 1
        else:
            return primes[mid]
    if target < primes[mid]:
        return find_closest(primes[mid - 1], primes[mid], target)
    else:
        return find_closest(primes[mid], primes[mid + 1], target)


def find_closest(valueA, valueB, target):
    if abs(target - valueA) == abs(target - valueB):
        return valueA if valueA < valueB else valueB
    return valueA if abs(target - valueA) < abs(target - valueB) else valueB


def get_magical_word(string):
    magical_word = ''
    for char in string:
        magical_word += chr(nearest_magical_char(ord(char)))
    return magical_word


def main():
    noOfTestCases = int(input())
    testCases = []
    for iterator in range(noOfTestCases):
        length = int(input())
        string = input().strip()
        testCases.append({'length': length, 'string': string})
    for iterator in range(noOfTestCases):
        print(get_magical_word(testCases[iterator]['string']))


if __name__ == '__main__':
    main()
