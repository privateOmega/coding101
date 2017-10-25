def roundToFive(x):
	rem = x % 5
	if rem >= 3: 
		print((x+(5-rem)))
	else:
		print(x)
	return	

n = int(input().strip())
arr = []
for x in range(n):
	arr.append(int(input().strip()))
for x in range(n):
	if arr[x] >= 38:
		roundToFive(arr[x])
	else:
		print(arr[x])
