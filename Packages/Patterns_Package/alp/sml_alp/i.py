def for_i():
        """ Pattern of Small Alphabet: 'i' using for loop """
        for i in range(7):
                for j in range(5):
                        if i==6 or j==2 and i>1 or i==2 and j<3 or i==0 and j==2:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_i():
        """ Pattern of Small Alphabet: 'i' using while loop """
        i=0
        while i<7:
                j=0
                while j<5:
                        if i==6 or j==2 and i>1 or i==2 and j<3 or i==0 and j==2:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
