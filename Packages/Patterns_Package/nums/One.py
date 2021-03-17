def for_One():
        """ Pattern of Number : '1' using for loop """
        for i in range(7):
                for j in range(5):
                        if j==2 or i+j==2 or i==6:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_One():
        """ Pattern of Number : '1' using while loop """
        i=0
        while i<7:
                j=0
                while j<5:
                        if j==2 or i+j==2 or i==6:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
