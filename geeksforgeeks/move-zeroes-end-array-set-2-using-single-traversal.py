from typing import Optional, List


def move_zeroes_to_end(array: Optional[List[int]] = None):
    array_length = len(array)

    j = 0

    for i in range(array_length):
        if array[i] != 0:
            array[i], array[j] = array[j], array[i]
            j += 1


if __name__ == "__main__":
    array = [0, 1, 9, 8, 4, 0]
    move_zeroes_to_end(array)
    print(array)
