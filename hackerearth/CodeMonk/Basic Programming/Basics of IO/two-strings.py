def is_equal(stringA, stringB):
    dictA = {char: stringA.count(char) for char in set(stringA)}
    dictB = {char: stringB.count(char) for char in set(stringB)}
    if dictA == dictB:
        return 'YES'
    return 'NO'


def main():
    noOfTestCases = int(input())
    testCases = []
    for iterator in range(noOfTestCases):
        stringArray = input().strip().split(' ')
        testCases.append(
            {'stringA': stringArray[0], 'stringB': stringArray[1]})
    for iterator in range(noOfTestCases):
        print(is_equal(testCases[iterator]['stringA'],
                       testCases[iterator]['stringB']))


if __name__ == '__main__':
    main()

""" 
Given two strings of equal length, you have to tell whether they both strings are identical.

Two strings S1 and S2 are said to be identical, if any of the permutation of string S1 is equal to the string S2. See Sample explanation for more details.

Input :

First line, contains an intger 'T' denoting no. of test cases.
Each test consists of a single line, containing two space separated strings S1 and S2 of equal length.
Output:

For each test case, if any of the permutation of string S1 is equal to the string S2 print YES else print NO.
Constraints:

1<= T <=100
1<= |S1| = |S2| <= 10^5
String is made up of lower case letters only.
Note : Use Hashing Concept Only . Try to do it in O(string length) . """
