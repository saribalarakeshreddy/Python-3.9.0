def for_Right_faced_equilataral_angle_Triangle():
    """ pattern for : Right_faced_equilataral_angle_Triangle"""
    for i in range(7):
        for j in range(4):
            if j==0 or i==j or i+j==6:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
def while_Right_faced_equilataral_angle_Triangle():
    """ pattern for : Right_faced_equilataral_angle_Triangle"""
    i=0
    while i<7:
        j=0
        while j<4:
            if j==0 or i==j or i+j==6:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            j+=1
        i+=1
        print()