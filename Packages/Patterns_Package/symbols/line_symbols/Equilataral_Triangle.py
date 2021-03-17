def for_Equlatoral_Triangle():
	""" Pattern for : Equlatoral_Triangle using for loop"""
	for i in range(5):
		for j in range(9):
			if i+j==4 or j-i==4 or i==4:
				print('*',end=' ')
			else:
				print(' ',end=' ')
		print()
def while_Equlatoral_Triangle():
	""" Pattern for : Equlatoral_Triangle using while loop"""
	i=0
	while i<5:
		j=0
		while j<9:
			if i+j==4 or j-i==4 or i==4:
				print('*',end=' ')
			else:
				print(' ',end=' ')
			j+=1
		i+=1
		print()
