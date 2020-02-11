from typing import Optional, List


def merge_sort(array: Optional[List[int]] = None):
    array_length = len(array)
    if array_length > 1:
        mid = array_length // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


def print_array(array: Optional[List[int]] = None):
    for iterator in array:
        print(iterator, end=" ")
    print()


if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7]
    print_array(array)
    merge_sort(array)
    print_array(array)
