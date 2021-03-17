def for_Nine():
        """ Pattern of Number: '9' using for loop """
        for i in range(7):
                for j in range(5):
                        if i%3==0 and j in(1,2,3) or j==0 and i in(1,2) or j==4 and i%3!=0:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_Nine():
        """ Pattern of Number: '9' using while loop """
        i=0
        while i<7:
                j=0
                while j<5:
                        if i%3==0 and j in(1,2,3) or j==0 and i in(1,2) or j==4 and i%3!=0:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()

