def simpleArraySum(arr):
	return sum(arr)

n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
print(simpleArraySum(arr))
