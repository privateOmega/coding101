def solve(a0, a1, a2, b0, b1, b2):
	p1, p2 = 0, 0
	if a0>b0:
		p1+=1
	elif a0<b0:
		p2+=1
	if a1>b1:
		p1+=1
	elif a1<b1:
		p2+=1
	if a2>b2:
		p1+=1
	elif a2<b2:
		p2+=1
	return p1,p2
	

a0, a1, a2 = map(int, input().strip().split(' '))
b0, b1, b2 = map(int, input().strip().split(' '))
p1, p2 = solve(a0, a1, a2, b0, b1, b2)
print(p1, p2)
