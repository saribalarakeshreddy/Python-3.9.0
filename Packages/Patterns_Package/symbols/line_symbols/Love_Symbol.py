def for_Love_symbol():
    """ pattern for :Love_symbol using for loop"""
    for i in range(6):
        for j in range(7):
            if i+j==8 or i-j==2 or (i==0 and j%3!=0) or (i==1 and j%3==0):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
def while_Love_symbol():
    """ pattern for :Love_symbol using while loop"""
    i=0
    while i<6:
        j=0
        while j<7:
            if i+j==8 or i-j==2 or (i==0 and j%3!=0) or (i==1 and j%3==0):
                print('*',end=' ')
            else:
                print(' ',end=' ')
            j+=1
        i+=1
        print()