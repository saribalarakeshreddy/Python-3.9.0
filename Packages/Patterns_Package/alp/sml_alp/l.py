def for_l():
        """ Pattern of Small Alphabet: 'l' using for loop """
        for i in range(9):
                for j in range(5):
                        if j==2 or i+j==2 or i+j==11:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_l():
        """ Pattern of Small Alphabet: 'l' using while loop """
        i=0
        while i<9:
                j=0
                while j<5:
                        if j==2 or i+j==2 or i+j==11:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
