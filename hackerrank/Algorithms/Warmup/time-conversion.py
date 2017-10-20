def timeconversion(t):
	time = t[:-2]
	hh, mm, ss = time.split(':')	
	m = t[-2:]
	H = int(hh)
	if m == 'AM' and hh == '12':
		hh = '00'
		print(hh + ':' + mm + ':' + ss) 
	elif m == 'PM' and hh != '12':
		H += 12
		print(str(H) + ':' + mm + ':' + ss)
	elif m == 'PM' and hh == '12':
		print(hh + ':' + mm + ':' + ss)
	else:
		print(hh + ':' + mm + ':' + ss)

t = input().strip()
timeconversion(t)
