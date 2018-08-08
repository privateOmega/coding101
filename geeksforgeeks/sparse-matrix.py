def is_sparse(arr, rows, cols):
    count = 0
    for i in range(0, rows):
        for j in range(0, cols):
            if arr[i][j] == 0:
                count += 1
    return (count > (rows * cols)//2)


def main():
    arr = [[1, 0, 0, 4], [0, 0, 0, 1], [0, 1, 0, 0]]
    rows = 2
    cols = 4
    print('Matrix is sparse') if is_sparse(arr, rows, cols) else print('Matrix is non sparse')


if __name__ == '__main__':
    main()
