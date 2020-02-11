""" Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place. """

# naive-approach
""" def find_lowest_missing_postive_integer(array):
    s = set(array)
    iterator = 1
    while True:
        if iterator not in s:
            print("lowest missing positive integer is {}".format(iterator))
            break
        iterator += 1 """

def find_lowest_missing_postive_integer(array):
    largest_element = max(array)
    if largest_element < 1:
        return 1
    
    if len(array) == 1:
        return 2 if array[0] == 1 else 1

    
    positive_array = filter(lambda x: x >= 0, array)
    index_array = [0] * largest_element
    for element in positive_array:
        index_array[element - 1] = 1
    
    for index in range(len(index_array)):
        if index_array[index] == 0:
            return index + 1
    return index + 2



if __name__ == "__main__":
    array = [3, 4, -1, 1]
    print(find_lowest_missing_postive_integer(array))
    array = [1, 2, 0]
    print(find_lowest_missing_postive_integer(array))