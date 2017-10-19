no = int(input().strip())
arr = [int(a) for a in input().strip().split(' ')]

p, n, z = 0, 0, 0
for a in arr:
	if a > 0:
		p += 1
	elif a < 0:
		n += 1
	elif a == 0:
		z += 1

print("%0.6f"%(p/no))
print("%0.6f"%(n/no))
print("%0.6f"%(z/no))
 
