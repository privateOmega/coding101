""" Given an array (or string), the task is to reverse the array/string. """

from typing import Optional, List


def reverse_list(array: Optional[List[int]] = None):
    if array is None:
        return

    array_length = len(array)

    start, end = 0, array_length - 1

    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6]
    reverse_list(array)
    print(array)
