def for_k():
        """ Pattern of Small Alphabet: 'k' using for loop """
        for i in range(9):
                for j in range(4):
                        if j==0 or i+j==6 or i-j==5:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_k():
        """ Pattern of Small Alphabet: 'k' using while loop """
        i=0
        while i<9:
                j=0
                while j<4:
                        if j==0 or i+j==6 or i-j==5:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
