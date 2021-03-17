def for_Four():
        """ Pattern of Number: '4' using for loop """
        for i in range(6):
                for j in range(6):
                        if j==3 or i+j==3 or i==3:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_Four():
        """ Pattern of Number: '4' using while loop """
        i=0
        while i<6:
                j=0
                while j<6:
                        if j==3 or i+j==3 or i==3:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
