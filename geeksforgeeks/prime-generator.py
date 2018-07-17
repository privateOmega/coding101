from math import sqrt


def generate_n_primes(limit):
    primes = []
    number = 2
    while len(primes) < limit:
        has_factor = False
        for i in primes:
            if i <= sqrt(number) and number % i == 0:
                has_factor = True
                break
        primes += [] if has_factor else [number]
        number += 1
    return primes


def main():
    limit = 1000
    print(generate_n_primes(limit))


if __name__ == '__main__':
    main()
