n = int(input().strip())
arr = []
for i in range(n):
	j = [int(a) for a in input().strip().split(' ')]
	arr.append(j)

md, sd = 0, 0
for i in range(n):
	for j in range(n):
		if i == j:
			md += arr[i][j]
		if i == n-j-1:
			sd += arr[i][j]
			
print(abs(md-sd))
