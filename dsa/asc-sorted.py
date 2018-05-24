def check_sorted(A, n):
    if(n == 1):
        return 1
    return check_sorted(A, n-1) if A[n-1] > A[n-2] else 0


STR_ARR = input().split(' ')
ARR = [int(num) for num in STR_ARR]
VAL = check_sorted(ARR, len(ARR))
print('Sorted' if VAL != 0 else 'Unsorted')
