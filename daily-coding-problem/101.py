""" Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:

Input: 4
Output: 2 + 2 = 4


If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

[a, b] < [c, d]


If a < c OR a==c AND b < d. """

def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)]
    p = 2
    while(p * p <= n):
        if (primes[p] == True):
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    prime_list = []
    for iterator in range(2, n):
        if primes[iterator]:
            prime_list.append(iterator)

    return prime_list

def get_prime_set(number):
    for iterator in primes:
        diff = number - iterator
        if diff in primes:
            return [iterator, diff]

primes = sieve_of_eratosthenes(30)

prime_set = get_prime_set(30)

print(prime_set)