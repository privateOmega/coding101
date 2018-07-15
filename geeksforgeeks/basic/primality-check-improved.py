def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    # Starting from 25
    i = 5
    while i * i <= number:
        if(number % i == 0 or number % (i+2) == 0):
            return False
        i = i+6
    return True


def main():
    number = 5
    if is_prime(number):
        print(number, "is prime")
    else:
        print(number, "is not prime")


if __name__ == '__main__':
    main()
