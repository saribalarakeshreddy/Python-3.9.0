def  for_Right_faced_Right_angle_Triangle():
    """ pattern for: Right_faced_Right_angle_Triangle using for loop"""
    for i in range(7):
        for j in range(7):
            if i==6 or j==0 or i==j:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
def  while_Right_faced_Right_angle_Triangle():
    """ pattern for: Right_faced_Right_angle_Triangle using while loop"""
    i=0
    while i<7:
        j=0
        while j<7:
            if i==6 or j==0 or i==j:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            j+=1
        i+=1
        print()