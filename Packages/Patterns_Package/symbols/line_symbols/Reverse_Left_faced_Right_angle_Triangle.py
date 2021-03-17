def for_Reverse_Left_faced_Right_angle_Triangle():
	""" Pattern for : Reverse_Left_faced_Right_angle_Triangle using for loop"""
	for i in range(7):
		for j in range(7):
			if i==0 or j==6 or i==j:
				print('*',end=' ')
			else:
				print(' ',end=' ')
		print()
def while_Reverse_Left_faced_Right_angle_Triangle():
	""" Pattern for : Reverse_Left_faced_Right_angle_Triangle using while loop"""
	i=0
	while i<7:
		j=0
		while j<7:
			if i==0 or j==6 or i==j:
				print('*',end=' ')
			else:
				print(' ',end=' ')
			j+=1
		i+=1
		print()