def for_J():
        """ Pattern of Captital Alphabet: 'J' using for loop"""
        for i in range(7):
                for j in range(4):
                        if j==3 and i<6 or i==0 or i==6 and j in(1,2) or i==5 and j==0:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_J():
        """ Pattern of Captital Alphabet: 'J' using while loop"""
        i=0
        while i<7:
                j=0
                while j<4:
                        if j==3 and i<6 or i==0 or i==6 and j in(1,2) or i==5 and j==0:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
