def for_y():
        """ Pattern of Small Alphabet: 'y' using for loop """
        for i in range(8):
                for j in range(4):
                        if j==3 and i<7 or j==0 and i in(0,1,2,6) or i==3 and j>0 or i==7 and j in(1,2):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_y():
        """ Pattern of Small Alphabet: 'y' using while loop """
        i=0
        while i<8:
                j=0
                while j<4:
                        if j==3 and i<7 or j==0 and i in(0,1,2,6) or i==3 and j>0 or i==7 and j in(1,2):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
