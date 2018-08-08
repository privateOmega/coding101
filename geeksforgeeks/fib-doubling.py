def fib_doubling(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fib_doubling(n >> 1)
        c = a * ((b << 1) - a)
        d = a * a + b * b
        if n & 1:
            return (d, c+d)
        else:
            return (c, d)


def main():
    print(fib_doubling(5)[0])


if __name__ == '__main__':
    main()
