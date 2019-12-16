""" Given two strings A and B, return whether or not A can be shifted some number of times to get B.
For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false. """

def shift_check(a, b):
    length = len(a)
    for shift in range(1, length):
        first = a[0]
        second = a[1:]
        a = second + first
        if a == b:
            print(True)
            return

    print(False)

shift_check('abcde', 'cdeab')
shift_check('abc', 'acb')