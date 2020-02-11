from typing import Optional, List


def modify_array(array: Optional[List[int]] = None):
    array_length = len(array)

    prev = array[0]
    array[0] = prev * array[1]

    for index in range(1, array_length - 1):
        current = array[index]
        array[index] = prev * array[index + 1]
        prev = current

    array[array_length - 1] = prev * array[array_length - 1]


if __name__ == "__main__":
    array = [2, 3, 4, 5, 6]
    modify_array(array)
    print(array)
