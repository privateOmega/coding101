from math import sqrt


def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)]
    primes[0] = primes[1] = False
    for i in range(2,  int(sqrt(n))+1):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                if primes[j]:
                    primes[j] = False
    for i in range(n):
        if primes[i]:
            print i


def main():
    sieve_of_eratosthenes(30)


if __name__ == '__main__':
    main()
