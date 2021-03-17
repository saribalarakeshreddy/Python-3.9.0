def for_M():
        """ Pattern of Captital Alphabet: 'M' using for loop"""
        for i in range(6):
                for j in range(7):
                        if j==0 or j==6  or (j-i==1 or i+j==5)  and i<3:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_M():
        """ Pattern of Captital Alphabet: 'M' using while loop"""
        i=0
        while i<6:
                j=0
                while j<7:
                        if j==0 or j==6  or (j-i==1 or i+j==5)  and i<3:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
