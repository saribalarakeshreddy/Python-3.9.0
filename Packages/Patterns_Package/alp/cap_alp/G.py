def for_G():
        """ Pattern of Captital Alphabet: 'G' using for loop"""
        for i in range(5):
                for j in range(6):
                        if i%4==0 and j not in(0,5) or j==0 and i not in(0,4) or j==5 and i in(2,3) or i==2 and j>1:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_G():
        """ Pattern of Captital Alphabet: 'G' using while loop"""
        i=0
        while i<5:
                j=0
                while j<6:
                        if i%4==0 and j not in(0,5) or j==0 and i not in(0,4) or j==5 and i in(2,3) or i==2 and j>1:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
