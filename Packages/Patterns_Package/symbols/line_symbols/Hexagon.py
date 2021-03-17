def for_Hexagon():
	""" pattern for : Hexagon using for loop"""
	for i in range(15):
		for j in range(11):
			if i+j==5 or j-i==5 or i-j==9 or i+j==19 or (j==0 or j==10) and i in range(6,10):
				print('*',end='  ')
			else:
				print('  ',end=' ')
		print()
def while_Hexagon():
	""" pattern for : Hexagon using while loop"""
	i=0
	while i<15:
		j=0
		while j<11:
			if i+j==5 or j-i==5 or i-j==9 or i+j==19 or (j==0 or j==10) and i in range(6,10):
				print('*',end='  ')
			else:
				print('  ',end=' ')
			j+=1
		i+=1		
		print()
