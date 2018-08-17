def count_divisors(lValue, rValue, kValue):
    count = 0
    for iterator in range(lValue, rValue+1):
        if iterator % kValue == 0:
            count += 1
    print(count)


def main():
    array = list(map(int, input().strip().split(' ')))
    count_divisors(array[0], array[1], array[2])


if __name__ == '__main__':
    main()

""" You have been given 3 integers - l, r and k. Find how many numbers between l and r (both inclusive) are divisible by k. You do not need to print these numbers, you just have to find their count.

Input Format
The first and only line of input contains 3 space separated integers l, r and k.

Output Format
Print the required answer on a single line. """