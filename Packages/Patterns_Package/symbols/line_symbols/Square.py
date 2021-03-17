def for_Square():
	""" Pattern for : Square using for loop"""
	for i in range(7):
		for j in range(7):
			if i in (0,6) or j in(0,6):
				print('*',end=' ')
			else:
				print(' ',end=' ')
		print()
def while_Square():
	""" Pattern for : Square using while loop"""
	i=0
	while i<7:
		j=0
		while j<7:
			if i in (0,6) or j in(0,6):
				print('*',end=' ')
			else:
				print(' ',end=' ')
			j+=1
		i+=1
		print()