""" Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

from typing import Dict, Optional
from string import ascii_lowercase

# Bruteforce Approach
""" def count_characters(string: str) -> int:
    return len(set(string))

def longest_substring(string: str, k: int) -> Optional[str]:
    sub_string_list = []
    for start_index in range(len(string)):
        for end_index in range(start_index + 1, len(string) + 1):
            sub_string = string[start_index:end_index]
            if count_characters(sub_string) == k:
                sub_string_list.append(sub_string)

    return max(sub_string_list, key=len) """

def isNotValid(k: int, count_dict: Optional[Dict] = None) -> bool:
    val = len([k for k,v in count_dict.items() if v != 0])
    print(k, val)
    return k < val


def longest_substring(string: str, k: int) -> Optional[str]:
    count_dict: Dict = dict.fromkeys(ascii_lowercase, 0)
    current_start: int = 0
    current_end: int = 0
    
    for character in string:
        count_dict[character] += 1
        current_end += 1

        while isNotValid(k, count_dict):
            count_dict[string[current_start]] -= 1
            current_start += 1
        
        print(character, current_start, current_end)
    
    return string[current_start:current_end]

    


if __name__ == "__main__":
    print(longest_substring('abcba', 2))
