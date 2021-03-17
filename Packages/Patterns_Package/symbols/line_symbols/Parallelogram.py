def for_Parallelogram():
	""" pattern for : Parallelogram using for loop """
	for i in range(7):
		for j in range(15):
			if i+j==6 or i==0 and j>6 or i+j==14 or i==6 and j<8:
				print('*',end='  ')
			else:
				print('  ',end=' ')
		print()
def while_Parallelogram():
	""" pattern for : Parallelogram using while loop """
	i=0
	while i<7:
		j=0
		while j<15:
			if i+j==6 or i==0 and j>6 or i+j==14 or i==6 and j<8:
				print('*',end='  ')
			else:
				print('  ',end=' ')
			j+=1
		i+=1
		print()
