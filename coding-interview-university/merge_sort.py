import math

def merge(A, B):
    if len(A) == 0:
        return B
    if len(B) == 0:
        return A
    if A[0] < B[0]:
        return [A[0]] + merge(A[1:], B)
    else:
        return [B[0]] + merge(A, B[1:])

def merge_sort(A, n):
    if n == 1:
        return A
    middle = math.floor(n/2)
    left_half = A[:middle]
    right_half = A[middle:]
    return merge(merge_sort(left_half, middle), merge_sort(right_half, n - middle))

if __name__ == "__main__":
    A = [1, 2, 4, 5, 0]
    B = merge_sort(A, len(A))
    print(B)