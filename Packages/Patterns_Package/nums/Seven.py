def for_Seven():
        """ Pattern of Number: '7' using for loop"""
        for i in range(7):
                for j in range(5):
                        if i==0 or i+j==5:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_Seven():
        """ Pattern of Number: '7' using while loop"""
        i=0
        while i<7:
                j=0
                while j<5:
                        if i==0 or i+j==5:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
