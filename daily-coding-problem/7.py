""" Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'. """

def is_char(code):
    return 0 if code > 26 or code < 1 else 1

def count_decode(string):
    if len(string) and string[0] == '0':
        return 0
    if len(string) <= 1:
        return 1
    else:
        count = count_decode(string[1:])
        if is_char(int(string[:2])):
             count += count_decode(string[2:])
        return count


if __name__ == "__main__":
    print(count_decode('111'))