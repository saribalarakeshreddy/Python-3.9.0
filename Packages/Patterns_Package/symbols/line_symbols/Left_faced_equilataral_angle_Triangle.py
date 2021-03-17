def for_Left_faced_equilataral_angle_Triangle():
    """ pattern for : Left_faced_equilataral_angle_Triangle using for loop"""
    for i in range(7):
        for j in range(4):
            if j==3 or i+j==3 or i-j==3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
def while_Left_faced_equilataral_angle_Triangle():
    """ pattern for : Left_faced_equilataral_angle_Triangle using while loop"""
    i=0
    while i<7:
        j=0
        while j<4:
            if j==3 or i+j==3 or i-j==3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            j+=1
        i+=1
        print()