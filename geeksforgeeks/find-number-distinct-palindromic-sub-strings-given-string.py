
from typing import Optional, List


""" def find_substrings(string: str) -> Optional[List[str]]:
    string_length = len(string)
    substrings = set()
    for first_iterator in range(string_length):
        for second_iterator in range(first_iterator+1, string_length + 1):
            substrings.add(string[first_iterator:second_iterator])

    return list(substrings)


def is_palindrome(string: str) -> bool:
    return string == string[::-1]


def find_palindromic_substrings(string: str) -> Optional[List[str]]:
    substrings = find_substrings(string)

    return list(filter(is_palindrome, substrings))
 """


def find_palindromic_substrings(string: str) -> Optional[List[str]]:
    palindromes = set()
    string_length = len(string)

    for index, character in enumerate(string):

        # odd palindrome
        start, end = index - 1, index + 1
        while start >= 0 and end < string_length and string[start] == string[end]:
            palindromes.add(string[start: end + 1])
            start -= 1
            end += 1

        # even palindrome
        start, end = index, index + 1
        while start >= 0 and end < string_length and string[start] == string[end]:
            palindromes.add(string[start: end + 1])
            start -= 1
            end += 1

        palindromes.add(character)

    return list(palindromes)


if __name__ == "__main__":
    print(find_palindromic_substrings("ammadmalayalam"))
