def for_h():
        """ Pattern of Small Alphabet: 'h' using for loop """
        for i in range(7):
                for j in range(5):
                        if j==0 or i==3 and j<4 or j==4 and i>3:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_h():
        """ Pattern of Small Alphabet: 'h' using while loop """
        i=0
        while i<7:
                j=0
                while j<5:
                        if j==0 or i==3 and j<4 or j==4 and i>3:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
