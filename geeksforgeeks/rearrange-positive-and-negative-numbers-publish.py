from typing import Optional, List


def rearrange(array: Optional[List[int]] = None):
    array_length = len(array)

    j = 0

    for i in range(array_length):
        if array[i] < 0:
            array[i], array[j] = array[j], array[i]
            j += 1

    neg, pos = 0, j

    while pos < array_length and neg < pos and array[neg] < 0:
        array[neg], array[pos] = array[pos], array[neg]

        pos += 1
        neg += 2


if __name__ == "__main__":
    array = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    rearrange(array)
    print(array)
