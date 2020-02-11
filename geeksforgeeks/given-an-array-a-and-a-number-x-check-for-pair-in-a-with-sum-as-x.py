""" Write a program that, given an array A[] of n numbers and another number x, determines whether or not there exist two elements in S whose sum is exactly x. """


from heapq import heapify
from typing import Optional, List, Tuple


""" def find_sum_pair(sum: int, array: Optional[List[int]]) -> Optional[Tuple[int, int]]:
    if not array:
        return
    heapify(array)
    array_length = len(array)
    left = 0
    right = array_length - 1

    while left < right:
        if array[left] + array[right] == sum:
            return array[left], array[right]
        elif array[left] + array[right] < sum:
            left += 1
        else:
            right -= 1
 """


def find_sum_pair(sum: int, array: Optional[List[int]]) -> Optional[Tuple[int, int]]:
    if not array:
        return
    difference_set = set()
    for element in array:
        difference = sum - element
        if element in difference_set:
            return element, difference
        difference_set.add(difference)


if __name__ == "__main__":
    print(find_sum_pair(16, [1, 4, 45, 6, 10, -8]))
