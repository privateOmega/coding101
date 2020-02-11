""" Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements. """

from typing import Optional, List


""" def rotate_array_by_one(array: Optional[List[int]] = None) -> Optional[List[int]]:
    array_length = len(array)

    temporary_variable = array[0]
    for index in range(array_length - 1):
        array[index] = array[index + 1]

    array[array_length - 1] = temporary_variable


def rotate_array(rotations: int, array: Optional[List[int]] = None) -> Optional[List[int]]:
    if array is None:
        return

    array_length = len(array)
    for iterator in range(rotations):
        rotate_array_by_one(array)

    return array """


""" def rotate_array(rotations: int, array: Optional[List[int]] = None) -> Optional[List[int]]:
    if array is None:
        return

    first_part = array[:rotations]
    first_part.reverse()
    second_part = array[rotations:]
    second_part.reverse()

    array = first_part + second_part
    array.reverse()

    return array """


def compute_gcd(first_number: int, second_number: int) -> int:
    while second_number:
        first_number, second_number = second_number, first_number % second_number

    return first_number


def rotate_array(rotations: int, array: Optional[List[int]] = None) -> Optional[List[int]]:
    if array is None:
        return

    array_length = len(array)

    gcd = compute_gcd(rotations, array_length)

    for set_index in range(gcd):
        temporary_variable = array[set_index]
        first_iterator = set_index
        while True:
            second_iterator = first_iterator + rotations
            if second_iterator >= array_length:
                second_iterator = second_iterator - array_length
            if second_iterator == set_index:
                break
            array[first_iterator] = array[second_iterator]
            first_iterator = second_iterator
        array[first_iterator] = temporary_variable

    return array


if __name__ == "__main__":
    print(rotate_array(3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
