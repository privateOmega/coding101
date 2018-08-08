from math import sqrt


def generate_n_primes(limit):
    primes = []
    number = 2
    while len(primes) < limit:
        has_factor = False
        for iterator in primes:
            if iterator <= sqrt(number) and number % iterator == 0:
                has_factor = True
                break
        primes += [] if has_factor else [number]
        number += 1
    return primes


def main():
    noOfTestCases = int(input())
    testCases = []
    if noOfTestCases < 1:
        return
    for iterator in range(noOfTestCases):
        testCases.append(int(input()))
    for iterator in range(noOfTestCases):
        print(" ".join(str(x) for x in generate_n_primes(testCases[iterator])))


if __name__ == '__main__':
    main()
