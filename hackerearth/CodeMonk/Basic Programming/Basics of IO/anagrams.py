def count_non_common(stringA, stringB):
    count = 0
    dictA = {char: stringA.count(char) for char in set(stringA)}
    dictB = {char: stringB.count(char) for char in set(stringB)}
    for char in dictA:
        if char in dictB:
            count += (dictA[char] if dictA[char] <
                      dictB[char] else dictB[char])
    print(len(stringA) + len(stringB) - (2 * count))


def main():
    noOfTestCases = int(input())
    testCases = []
    if noOfTestCases < 1:
        return
    for iterator in range(noOfTestCases):
        stringA = input()
        stringB = input()
        testCases.append({'stringA': stringA, 'stringB': stringB})
    for iterator in range(noOfTestCases):
        count_non_common(testCases[iterator]['stringA'],
                         testCases[iterator]['stringB'])


if __name__ == '__main__':
    main()


""" Given two strings, a and b , that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.

Input :

test cases,t
two strings a and b, for each test case
Output:

Desired O/p

Constraints :

string lengths<=10000

Note :

Anagram of a word is formed by rearranging the letters of the word.

For e.g. -> For the word RAM - MAR,ARM,AMR,RMA etc. are few anagrams.

SAMPLE INPUT 
1
cde
abc
SAMPLE OUTPUT 
4 """