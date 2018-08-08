def linear_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1


def jump_search(arr, block_size, element):
    prev_end = 0
    if block_size > len(arr):
        return -1
    for i in range(block_size, len(arr)-1, block_size):
        print(element, arr[prev_end], arr[i])
        if element > arr[prev_end] and element < arr[i]:
            result = linear_search(arr[prev_end:i+1], element)
            if(result != -1):
                return result + prev_end
            else:
                return -1
        else:
            prev_end = i
    return -1


def main():
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    block_size = 4
    element = 55
    result = jump_search(arr, block_size, element)
    if result != -1:
        print ("Element is present at index", result)
    else:
        print("Element is not present in array")


if __name__ == '__main__':
    main()
