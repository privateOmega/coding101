s, t = map(int, input().strip().split(' '))
a, b = map(int, input().strip().split(' '))
m, n = map(int, input().strip().split(' '))
apples = list(map(int, input().strip().split(' ')))
oranges = list(map(int, input().strip().split(' ')))
cApples, cOranges = 0, 0
for i in range(m):
	tApples = a + apples[i]
	if tApples >= s and tApples <= t:
		cApples = cApples + 1
for i in range(n):
	tOranges = b + oranges[i]
	if tOranges <= t and tOranges >= s:
		cOranges = cOranges + 1
print(cApples)
print(cOranges)
