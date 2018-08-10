def search_numpad(item):
    numpad = {
        1: ['.', ',', '?', '!', '1'],
        2: ['a', 'b', 'c', '2'],
        3: ['d', 'e', 'f', '3'],
        4: ['g', 'h', 'i', '4'],
        5: ['j', 'k', 'l', '5'],
        6: ['m', 'n', 'o', '6'],
        7: ['p', 'q', 'r', 's', '7'],
        8: ['t', 'u', 'v', '8'],
        9: ['w', 'x', 'y', 'z', '9'],
        0: ['_', '0']
    }
    for key, keyArray in numpad.items():
        for index, value in enumerate(keyArray):
            if value == item:
                return key, index+1


def track_movements(valueString):
    movements = 0
    lastKey = 1
    for character in valueString:
        key, operationCount = search_numpad(character)
        movements = movements + operationCount
        keyMovements = find_matrix_movements(lastKey, key)
        movements = movements + keyMovements
        lastKey = key
    return movements


def find_matrix_position(item):
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
    for iteratorA in range(len(matrix)):
        for iteratorB in range(len(matrix[iteratorA])):
            if matrix[iteratorA][iteratorB] == item:
                return (iteratorA, iteratorB)


def find_matrix_movements(lastKey, newKey):
    xA, yA = find_matrix_position(lastKey)
    xB, yB = find_matrix_position(newKey)
    if xA == xB and yA == yB:
        return 0
    else:
        return max(abs(xA-xB), abs(yB-yA))  # Chebyshev distance


def main():
    noOfTestCases = int(input())
    testCases = []
    if noOfTestCases < 1:
        return
    for iterator in range(noOfTestCases):
        testCases.append(input())
    for iterator in range(noOfTestCases):
        print(track_movements(testCases[iterator]))


if __name__ == '__main__':
    main()


""" You may be already familiar with the working of the keypad, however if you're not we shall see a few examples.

To type "b", we need to press "2" twice. To type "?" we need to press "1" thrice. To type "5" we need to press "5" four times. To type "0" we need to press "0" twice.

I hope that it's clear how the keypad is being used.

Now Roy has lot of text messages and they are pretty lengthy. So he devised a mechanical-hand-robot (with only 1 finger) which does the typing job. One drawback of this robot is its typing speed. It takes 1 second for single press of any button. Also it takes 1 second to move from one key to another. Initial position of the hand-robot is at key 1.

So if its supposed to type "hack" it will take 1 second to move from key 1 to key 4 and then 2 seconds to type "h".
Now again 1 second to move from key 4 to key 2 and then 1 second to type "a".
Since "c" is present at the same key as "a" movement time is 0. So it simply takes 3 seconds to type "c".
Finally it moves from key 2 to key 5 in 1 second and then 2 seconds to type "k". So in total it took 1+2+1+1+3+1+2= 11 seconds to type "hack".

Input:
First line contains T - number of test cases.
Each of next T lines contain a string S - the message Roy needs to send.
Each string is terminated by a newline escape sequence \n.

Output:
For each test case output the time taken by the hand-robot to type down the message.

Constraints:
1 ≤ T ≤ 50
1 ≤ |S| ≤ 1000 , where |S| denotes the length of string S
String is made of all the characters shown in the image above which are as follows:
"." (period), "," (comma), "?" (question mark), "!" (exclamation mark), [a-z] (small case english alphabets), "_" (underscore) and [0-9] (digits)

Note: We are using "_" underscore instead of " " empty space to avoid confusion
 """
