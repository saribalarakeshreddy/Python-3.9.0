def for_Two():
        """ Pattern of Number : '2' using for loop"""
        for i in range(7):
                for j in range(5):
                        if i==6 or i+j==6 or i==0 and j not in(0,4) or i==1 and j in(0,4):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_Two():
        """ Pattern of Number : '2' using while loop"""
        i=0
        while i<7:
                j=0
                while j<5:
                        if i==6 or i+j==6 or i==0 and j not in(0,4) or i==1 and j in(0,4):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
