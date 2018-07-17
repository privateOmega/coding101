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


def main():
    arr = [2, 3, 4, 10, 40]
    element = 10
    result = binary_search(arr, 0, len(arr)-1, element)
    if result != -1:
        print ("Element is present at index", result)
    else:
        print("Element is not present in array")


if __name__ == '__main__':
    main()
