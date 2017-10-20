n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
print(arr.count(max(arr)))
