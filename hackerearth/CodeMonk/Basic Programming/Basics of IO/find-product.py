from math import pow


def calculate_product(array):
    answer = 1
    for iterator in range(len(array)):
        if(array[iterator] >= 1):
            answer = (answer * array[iterator]) % (pow(10, 9) + 7)
    print(int(answer))


def main():
    arrayLength = int(input())
    array = list(map(int, input().strip().split(' ')))
    calculate_product(array)


if __name__ == '__main__':
    main()


""" You have been given an array A of size N consisting of positive integers. You need to find and print the product of all the number in this array Modulo 10^9 + 7.

Input Format:
The first line contains a single integer N denoting the size of the array. The next line contains N space separated integers denoting the elements of the array

Output Format:
Print a single integer denoting the product of all the elements of the array Modulo .

SAMPLE INPUT 
5
1 2 3 4 5
SAMPLE OUTPUT 
120
Explanation
There are 5 integers to multiply. Let's store the final answer in  variable. Since 1 is identity value for multiplication, initialize  as 1.

So the process goes as follows:

answer = 1
answer = (answer * 1) % (10^9 + 7)
answer = (answer * 2) % (10^9 + 7)
answer = (answer * 3) % (10^9 + 7)
answer = (answer * 4) % (10^9 + 7)
answer = (answer * 5) % (10^9 + 7)

The above process will yield answer as 120 """
