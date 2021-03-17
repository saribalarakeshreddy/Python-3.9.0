def for_Q():
        """ Pattern of Captital Alphabet: 'Q' using for loop"""
        for i in range(7):
                for j in range(6):
                        if i%4==0 and j in(1,2,3) or j%4==0 and i in(1,2,3) or i==j and i>1:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_Q():
        """ Pattern of Captital Alphabet: 'Q' using while loop"""
        i=0
        while i<7:
                j=0
                while j<6:
                        if i%4==0 and j in(1,2,3) or j%4==0 and i in(1,2,3) or i==j and i>1:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
