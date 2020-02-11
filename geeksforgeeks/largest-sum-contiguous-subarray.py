from sys import maxsize


def maximum_subarray_sum(array=None):
    max_so_far = array[0]
    curr_max = array[0]

    for iterator in range(1, len(array)):
        curr_max = max(array[iterator], curr_max + array[iterator])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far


if __name__ == "__main__":
    array = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    print(maximum_subarray_sum(array))
