def for_j():
        """ Pattern of Small Alphabet: 'j' using for loop"""
        for i in range(8):
                for j in range(4):
                        if j==3 and i>1 and i<7 or i==2 or i==7 and j in(1,2) or i==6 and j==0 or j==3 and i==0:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_j():
        """ Pattern of Small Alphabet: 'j' using while loop"""
        i=0
        while i<8:
                j=0
                while j<4:
                        if j==3 and i>1 and i<7 or i==2 or i==7 and j in(1,2) or i==6 and j==0 or j==3 and i==0:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
