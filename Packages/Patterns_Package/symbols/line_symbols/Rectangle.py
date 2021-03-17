def for_Rectangle():
	""" Pattern for : Rectangle using for loop"""
	for i in range(7):
		for j in range(12):
			if i in (0,6) or j in(0,11):
				print('*',end=' ')
			else:
				print(' ',end=' ')
		print()
def while_Rectangle():
	""" Pattern for : Rectangle using while loop"""
	i=0
	while i<7:
		j=0
		while j<12:
			if i in (0,6) or j in(0,11):
				print('*',end=' ')
			else:
				print(' ',end=' ')
			j+=1
		i+=1
		print()