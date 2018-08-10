def factorial(number):
    result = [None] * 500
    result[0] = 1
    resultSize = 1
    for iterator in range(2, number + 1):
        result, resultSize = multiply(iterator, result, resultSize)
    for iterator in range(0, resultSize - 1, -1):
        print('iterator', iterator, resultSize)
        print(result)


def multiply(value, result, resultSize):
    carry = 0
    for iteratorA in range(0, resultSize):
        product = result[iteratorA] * value + carry
        result[iteratorA] = product % 10
        carry = product // 10
    while carry:
        result[resultSize] = carry % 10
        carry = carry/10
        resultSize = resultSize + 1
    return result, resultSize


def main():
    noOfTestCases = int(input())
    testCases = []
    if noOfTestCases < 1:
        return
    for iterator in range(noOfTestCases):
        testCases.append(int(input()))
    for iterator in range(noOfTestCases):
        factorial(testCases[iterator])


if __name__ == '__main__':
    main()
