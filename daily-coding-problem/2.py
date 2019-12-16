""" Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division? """

array = [1, 2, 3, 4, 5]

length = len(array)

left = [1] * length
right = [1] * length

for iterator in range(1, length):
    left[iterator] = left[iterator-1] * array[iterator-1]

for iterator in range(length - 2, -1, -1):
    right[iterator] = right[iterator + 1] * array[iterator + 1]

for iterator in range(0, length):
    array[iterator] = left[iterator] * right[iterator]

print(array)
