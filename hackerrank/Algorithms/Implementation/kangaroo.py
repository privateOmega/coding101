x1, v1, x2, v2 = map(int, input().strip().split(' '))
if((v1-v2)>0 and ((x2-x1)%(v1-v2)==0)):
	print("YES")
else:
	print("NO")
