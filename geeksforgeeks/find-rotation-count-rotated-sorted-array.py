from typing import Optional, List


""" def count_rotations(array: Optional[List[int]] = None) -> Optional[int]:
    if array is None:
        return

    minimum_element = array[0]
    minimum_index = 0
    for index, element in enumerate(array):
        if minimum_element > element:
            minimum_element = element
            minimum_index = index

    return minimum_index """


def count_rotations(low: int, high: int, array: Optional[List[int]] = None) -> Optional[int]:
    if array is None:
        return

    if high < low:
        return 0

    if high == low:
        return low

    mid = low + (high - low) // 2

    if mid < high and array[mid + 1] < array[mid]:
        return mid + 1

    if mid > low and array[mid] < array[mid - 1]:
        return mid

    if array[high] > array[mid]:
        return count_rotations(array, low, mid - 1)
    return count_rotations(array, mid + 1, high)


if __name__ == "__main__":
    array = [15, 18, 2, 3, 6, 12]
    array_length = len(array)
    print(count_rotations(0, array_length - 1, array))
