import numpy as np


def calculate_product_determinant(matrixA, matrixB):
    productMatrix = np.matmul(matrixA, matrixB)
    # print(productMatrix)
    determinant = np.linalg.det(productMatrix)
    return determinant


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
        print(iterator, int(round(calculate_product_determinant(
            testCases[iterator]['matrixA'], testCases[iterator]['matrixB']))))


if __name__ == '__main__':
    main()
