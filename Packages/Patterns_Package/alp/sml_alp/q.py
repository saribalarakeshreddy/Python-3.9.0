def for_q():
        """ Pattern of Small Alphabet: 'q' using for loop """
        for i in range(9):
                for j in range(6):
                        if i in (1,4) and j not in (0,4,5) or j==0 and i in (2,3) or j==3 or i+j==11 :
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_q():
        """ Pattern of Small Alphabet: 'q' using while loop """
        i=0
        while i<9:
                j=0
                while j<6:
                        if i in (1,4) and j not in (0,4,5) or j==0 and i in (2,3) or j==3 or i+j==11 :
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
