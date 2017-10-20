arr = list(map(int, input().strip().split(' ')))
arr.sort()
s = sum(arr)
print((s-arr[-1]),(s-arr[0]))
