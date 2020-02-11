from typing import Optional, List


""" def seggregate_odd_even(array: Optional[List[int]] = None):
    array_length = len(array)

    left, right = 0, array_length - 1

    while left < right:
        while array[left] % 2 == 0:
            left += 1
        while array[right] % 2 != 0:
            right -= 1

        if left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1 """


def seggregate_odd_even(array: Optional[List[int]] = None):
    array_length = len(array)

    j = -1

    for i in range(array_length):
        if array[i] % 2 == 0:
            j += 1

            array[i], array[j] = array[j], array[i]


if __name__ == "__main__":
    array = [12, 34, 45, 9, 8, 90, 3]
    seggregate_odd_even(array)
    print(array)
