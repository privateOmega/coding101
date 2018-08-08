def spiral_print(rows, cols, arr):
    rowStart, colStart, rowEnd, colEnd = 0, 0, rows, cols
    while (rowStart < rowEnd and colStart < colEnd):
        # Iterate from left to right
        for i in range(colStart, colEnd):
            print(arr[rowStart][i], end=' ')
        rowStart += 1
        # Iterate from top to bottom
        for i in range(rowStart, rowEnd):
            print(arr[i][colEnd-1], end=' ')
        colEnd -= 1
        # Iterate from right to left
        if rowStart < rowEnd:
            for i in range(colEnd-1, colStart-1, -1):
                print(arr[rowEnd-1][i], end=' ')
            rowEnd -= 1
        # Iterate from bottom to top
        if colStart < colEnd:
            for i in range(rowEnd-1, rowStart-1, -1):
                print(arr[i][colStart], end=' ')
            colStart += 1


def main():
    arr = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    rows = 3
    cols = 5
    spiral_print(rows, cols, arr)


if __name__ == '__main__':
    main()
