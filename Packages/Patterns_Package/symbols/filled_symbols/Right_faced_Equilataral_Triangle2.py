def for_Right_faced_Equilataral_Triangle2():
    """ pattern for :Right_faced_Equilataral_Triangle2 using for loop"""
    for i in range(7):
        for j  in range(4):
            if j==0 or i==3 or j==1 and i in range(1,6) or j==2 and i in(2,4):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
def while_Right_faced_Equilataral_Triangle2():
    """ pattern for :Right_faced_Equilataral_Triangle2 using while loop"""
    i=0
    while i<7:
        j=0
        while j<4:
            if j==0 or i==3 or j==1 and i in range(1,6) or j==2 and i in(2,4):
                print('*',end=' ')
            else:
                print(' ',end=' ')
            j+=1
        i+=1
        print()
