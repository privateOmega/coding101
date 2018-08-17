from functools import reduce


def execute_queries(array, query):
    if query[0] == 1 and query[1] < len(array):
        array[query[1]] = query[2]
    elif query[0] == 2:
        print(reduce((lambda x, y: x + y), array[query[1]: query[2] + 1]))
    return array


def main():
    arrayLength, noOfQueries = list(map(int, input().strip().split(' ')))
    array = list(map(int, input().strip().split(' ')))
    queries = []
    for iterator in range(noOfQueries):
        queries.append(list(map(int, input().strip().split(' '))))
    for iterator in range(noOfQueries):
        array = execute_queries(array, queries[iterator])


if __name__ == '__main__':
    main()
