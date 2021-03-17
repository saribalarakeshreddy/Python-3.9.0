def for_Five():
        """ Pattern of Number: '5' using for loop """
        for i in range(6):
                for j in range(5):
                        if i==0 or i==2 and j<4 or j==0 and i<3 or j==4 and i in(3,4) or i==5 and j<4 :
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_Five():
        """ Pattern of Number: '5' using while loop """
        i=0
        while i<6:
                j=0
                while j<5:
                        if i==0 or i==2 and j<4 or j==0 and i<3 or j==4 and i in(3,4) or i==5 and j<4 :
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
                        
