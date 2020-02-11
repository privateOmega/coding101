""" Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5. """


def non_adjacent_sum(array):
    incl, excl = 0, 0
    for element in array:
        excl, incl = max(incl, excl), excl + element

    return max(excl, incl)


if __name__ == "__main__":
    array = [2, 5, 3, 1, 7]
    print(non_adjacent_sum(array))
