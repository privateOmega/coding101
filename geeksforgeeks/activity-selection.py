def sort_by_finish(start, finish):
    index = list(range(len(start)))
    index.sort(key=finish.__getitem__)
    start[:] = [start[i] for i in index]
    finish[:] = [finish[i] for i in index]
    return start, finish


def activity_selection(start, finish):
    i = 0
    print(i, end=' ')
    for j in range(1, len(start)):
        if start[j] >= finish[i]:
            print(j, end=' ')
            i = j


def main():
    start = [0, 3, 1, 5, 5, 8]
    finish = [6, 4, 2, 7, 9, 9]
    start, finish = sort_by_finish(start, finish)
    print('New activity order')
    for i in range(len(start)):
        print(i, start[i], finish[i])
    print('Selected Activities')
    activity_selection(start, finish)


if __name__ == '__main__':
    main()
