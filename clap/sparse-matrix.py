def is_not_sparse(matrix, rows, cols):
    count = 0
    for iteratorA in range(0, rows):
        for iteratorB in range(0, cols):
            if matrix[iteratorA][iteratorB] == 0:
                count += 1
    return (count <= int((rows * cols) * 0.53))


def main():
    noOfTestCases = int(input())
    testCases = []
    if noOfTestCases < 1:
        return
    for iterator in range(noOfTestCases):
        rows = int(input())
        matrix = [[] for _ in range(rows)]
        for iteratorA in range(rows):
            matrix[iteratorA] = [float(iteratorB)
                                 for iteratorB in input().strip().split(" ")]
        testCases.append(
            {'matrix': matrix, 'rows': rows, 'cols': len(matrix[iteratorA])})
    for iterator in range(noOfTestCases):
        print('VALID') if is_not_sparse(testCases[iterator]['matrix'], testCases[iterator]['rows'], testCases[iterator]['cols']) else print('INVALID')


if __name__ == '__main__':
    main()
