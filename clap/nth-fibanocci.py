def fibanocci_doubling(number):
    if number == 0:
        return (0, 1)
    else:
        a, b = fibanocci_doubling(number >> 1)
        c = a * ((b << 1) - a)
        d = a * a + b * b
        if number & 1:
            return (d, c + d)
        else:
            return (c, d)


def main():
    noOfTestCases = int(input())
    testCases = []
    if noOfTestCases < 1:
        return
    for iterator in range(noOfTestCases):
        testCases.append(int(input()))
    for iterator in range(noOfTestCases):
        print(fibanocci_doubling(testCases[iterator])[1])


if __name__ == '__main__':
    main()
