from math import sqrt


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number))):
        if number % i == 0:
            return False
    return True


def main():
    number = 3
    if(is_prime(number)):
        print(number, "is prime")
    else:
        print(number, "is not prime")


if __name__ == '__main__':
    main()
