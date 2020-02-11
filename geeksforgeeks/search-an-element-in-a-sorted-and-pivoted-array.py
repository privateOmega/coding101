""" An element in a sorted array can be found in O(log n) time via binary search. But suppose we rotate an ascending order sorted array at some pivot unknown to you beforehand. So for instance, 1 2 3 4 5 might become 3 4 5 1 2. Devise a way to find an element in the rotated array in O(log n) time. """

from typing import Optional, List


def search_in_rotated_sorted_array(search_element: int, low: int, high: int, array: Optional[List[int]]) -> Optional[int]:
    if low > high:
        return None

    middle = (low + high) // 2

    if array[middle] == search_element:
        return middle

    if search_element >= array[low] and search_element <= array[middle]:
        return search_in_rotated_sorted_array(search_element, low, middle - 1, array)
    return search_in_rotated_sorted_array(search_element, middle + 1, high, array)


if __name__ == "__main__":
    array = [4, 5, 6, 7, 8, 9, 1, 2, 3]
    array_length = len(array)

    print(search_in_rotated_sorted_array(1, 0, array_length - 1, array))
