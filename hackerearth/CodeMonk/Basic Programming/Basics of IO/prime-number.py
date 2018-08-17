from math import sqrt


def sieve_of_eratosthenes(number):
    primes = [True for iterator in range(number + 1)]
    primes[0] = primes[1] = False
    for iteratorA in range(2, int(sqrt(number))+1):
        if primes[iteratorA]:
            for iteratorB in range(2*iteratorA, number + 1, iteratorA):
                if primes[iteratorB]:
                    primes[iteratorB] = False
    for iterator in range(number):
        if primes[iterator]:
            print(iterator, end=' ')


def main():
    number = int(input())
    if number <= 1:
        return
    sieve_of_eratosthenes(number)


if __name__ == '__main__':
    main()

""" You are given an integer N. You need to print the series of all prime numbers till N.

Input Format

The first and only line of the input contains a single integer N denoting the number till where you need to find the series of prime number.

Output Format

Print the desired output in single line separated by spaces. """