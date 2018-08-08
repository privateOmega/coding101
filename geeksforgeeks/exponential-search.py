def binary_search(arr, left, right, element):
    if left <= right:
        mid = (left + right)//2
        if arr[mid] == element:
            return mid
        elif (element < arr[mid]):
            return binary_search(arr, left, mid-1, element)
        else:
            return binary_search(arr, mid+1, right, element)
    else:
        return -1


def exponential_search(arr, length, element):
    i = 1
    while i < length and arr[i] <= element:
        i *= 2
    return binary_search(arr, i//2, min(i, length), element)


def main():
    arr = [2, 3, 4, 10, 40]
    element = 10
    result = exponential_search(arr, len(arr), element)
    if result != -1:
        print ("Element is present at index", result)
    else:
        print("Element is not present in array")


if __name__ == '__main__':
    main()
