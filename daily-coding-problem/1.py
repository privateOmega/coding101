""" Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass? """

array = [10, 15, 3, 7]
k = 17

s = set()

for element in array:
    diff = k - element
    if diff in s:
        print("Pair with sum is {} {}".format(element, diff))
        break
    s.add(element)
