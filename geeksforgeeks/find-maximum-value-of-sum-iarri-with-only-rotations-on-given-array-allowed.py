""" Given an array, only rotation operation is allowed on array. We can rotate the array as many times as we want. Return the maximum possbile of summation of i*arr[i]. """

from typing import Optional, List


def find_maximum_sum(array: Optional[List[int]] = None):
    if array is None:
        return

    array_length = len(array)

    array_sum = 0
    current_value = 0

    for index in range(array_length):
        array_sum += array[index]
        current_value += index * array[index]

    maximum_value = current_value

    for index in range(1, array_length):
        current_value = current_value + array_sum - \
            array_length * array[array_length - index]
        if current_value > maximum_value:
            maximum_value = current_value

    return maximum_value


if __name__ == "__main__":
    print(find_maximum_sum([10, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
