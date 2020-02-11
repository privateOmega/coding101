""" Given an array that is sorted and then rotated around an unknown point. Find if the array has a pair with a given sum ‘x’. It may be assumed that all elements in the array are distinct. """

from typing import Optional, List, Tuple


def find_pivot(array: List[int]) -> Optional[int]:
    array_length = len(array)

    for index in range(array_length - 1):
        if array[index] > array[index + 1]:
            return index


def find_sum_pair(sum: int, array: Optional[List[int]] = None) -> Optional[Tuple[int, int]]:
    if array is None:
        return

    sum_pairs = set()

    array_length = len(array)

    pivot = find_pivot(array)
    high, low = pivot, pivot + 1

    while high != low:
        if array[low] + array[high] == sum:
            sum_pairs.add((array[low], array[high]))
            if low == (array_length + high - 1) % array_length:
                return sum_pairs
            low = (low + 1) % array_length
            high = (array_length + high - 1) % array_length
        elif array[low] + array[high] < sum:
            low = (low + 1) % array_length
        else:
            high = (array_length + high - 1) % array_length


if __name__ == "__main__":
    print(find_sum_pair(16, [11, 15, 6, 7, 9, 10]))
