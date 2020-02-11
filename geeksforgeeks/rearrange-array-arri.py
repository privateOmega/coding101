""" Given an array of elements of length N, ranging from 0 to N – 1. All elements may not be present in the array. If element is not present then there will be -1 present in the array. Rearrange the array such that A[i] = i and if i is not present, display -1 at that place. """

from typing import Optional, List


""" def rearrange_array(array: Optional[List[int]] = None):
    array_length = len(array)

    array_set = set(array)

    for index in range(array_length):
        array[index] = index if index in array_set else -1 """


def rearrange_array(array: Optional[List[int]] = None):
    array_length = len(array)

    for index in range(array_length):
        if array[index] != -1 and array[index] != index:
            temporary_variable = array[index]

            while array[temporary_variable] != -1 and array[temporary_variable] != temporary_variable:
                swap_variable = array[temporary_variable]
                array[temporary_variable] = temporary_variable
                temporary_variable = swap_variable

            array[temporary_variable] = temporary_variable

            if array[index] != index:
                array[index] = -1


if __name__ == "__main__":
    array = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
    rearrange_array(array)
    print(array)
