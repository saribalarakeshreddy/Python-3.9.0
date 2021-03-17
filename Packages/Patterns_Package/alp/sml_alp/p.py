def for_p():
        """ Pattern of Small Alphabet: 'p' using for loop """
        for i in range(9):
                for j in range(4):
                        if i in (1,4) and j!=3 or j==0 or j==3 and i in(2,3):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_p():
        """ Pattern of Small Alphabet: 'p' using while loop """
        i=0
        while i<9:
                j=0
                while j<4:
                        if i in (1,4) and j!=3 or j==0 or j==3 and i in(2,3):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
                        
