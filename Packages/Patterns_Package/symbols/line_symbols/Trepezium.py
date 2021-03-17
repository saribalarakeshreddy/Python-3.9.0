def for_Trepezium():
	""" Pattern for : Trepezium using for loop"""
	for i in range(7):
		for j in range(20):
			if i==6 or i+j==6 or j-i==13 or i==0 and j in range(6,13):
				print('*',end=' ')
			else:
				print(' ',end=' ')
		print()
def while_Trepezium():
	""" Pattern for : Trepezium using while loop"""
	i=0
	while i<7:
		j=0
		while j<20:
			if i==6 or i+j==6 or j-i==13 or i==0 and j in range(6,13):
				print('*',end=' ')
			else:
				print(' ',end=' ')
			j+=1
		i+=1
		print()