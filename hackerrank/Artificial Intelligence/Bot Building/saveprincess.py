def displayPathtoPrincess(n, grid):
    pos = n // 2
    p = [0, 0]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'p':
                p = [row, col]

    a = pos - p[0]
    b = pos - p[1]
    aAbs = abs(a)
    bAbs = abs(b)
    while aAbs:
        if a > 0:
            print('UP')
        else:
            print('DOWN')
        aAbs = aAbs - 1

    while bAbs:
        if b > 0:
            print('LEFT')
        else:
            print('RIGHT')
        bAbs = bAbs - 1


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)