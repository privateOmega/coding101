""" Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds. """

from time import sleep


def foo():
    print("bar")


def scheduler(f, time):
    sleep(time//1000)
    f()

if __name__ == "__main__":
    scheduler(foo, 5000)