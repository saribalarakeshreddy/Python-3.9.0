def for_Rhombus():
    """ pattern for :Rhombus or Diamond using for loop"""
    for i in range(7):
        for j in range(7):
            if ((i+j>=3 and j-i<=3) and i<=3) or j==3 or i==4 and j%6!=0 or i==5 and j in (2,4):
                print('*', end =' ')
            else:
                print(' ', end=' ')
        print()
def while_Rhombus():
    """ pattern for :Rhombus or Diamond using while loop"""
    i=0
    while i<7:
        j=0
        while j<7:
            if ((i+j>=3 and j-i<=3) and i<=3) or j==3 or i==4 and j%6!=0 or i==5 and j in (2,4):
                print('*', end =' ')
            else:
                print(' ', end=' ')
            j+=1
        i+=1
        print()