def calculate_hadamard_sum(matrixA, matrixB, size):
    sum = 0
    for iteratorA in range(size):
        for iteratorB in range(size):
            sum += (matrixA[iteratorA][iteratorB]
                    * matrixB[iteratorA][iteratorB])
    return int(round(sum))


def main():
    noOfTestCases = int(input())
    testCases = []
    if noOfTestCases < 1:
        return
    for iterator in range(noOfTestCases):
        size = int(input())
        matrixA = [[0] * size for _ in range(size)]
        for iteratorA in range(size):
            matrixA[iteratorA] = [float(iteratorB)
                                  for iteratorB in input().strip().split(" ")]
        matrixB = [[0] * size for _ in range(size)]
        for iteratorA in range(size):
            matrixB[iteratorA] = [float(iteratorB)
                                  for iteratorB in input().strip().split(" ")]
        testCases.append(
            {'size': size, 'matrixA': matrixA, 'matrixB': matrixB})
    for iterator in range(noOfTestCases):
        print(calculate_hadamard_sum(
            testCases[iterator]['matrixA'], testCases[iterator]['matrixB'], testCases[iterator]['size']))


if __name__ == '__main__':
    main()
