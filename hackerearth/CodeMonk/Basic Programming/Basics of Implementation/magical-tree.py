def main():
    noOfTestCases = int(input())
    testCases = []
    values = []
    for iterator in range(noOfTestCases):
        testCases.append(input())
        values.append(eval(testCases[iterator]))
    print(max(values))


if __name__ == '__main__':
    main()
