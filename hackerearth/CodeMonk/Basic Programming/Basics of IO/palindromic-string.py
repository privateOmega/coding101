def is_palindrome(testString):
    reversedString = testString[::-1]
    if testString == reversedString:
        return True
    return False

def main():
    testString = input()
    print('YES') if is_palindrome(testString) else print('NO')


if __name__ == '__main__':
    main()


""" You have been given a String S. You need to find and print whether this string is a palindrome or not. If yes, print "YES" (without quotes), else print "NO" (without quotes).

Input Format
The first and only line of input contains the String S. The String shall consist of lowercase English alphabets only.

Output Format
Print the required answer on a single line.


Note
String S consists of lowercase English Alphabets only.

SAMPLE INPUT 
aba
SAMPLE OUTPUT 
YES """