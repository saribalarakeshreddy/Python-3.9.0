def for_s():
        """ Pattern of Small Alphabet: 's' using for loop """
        for i in range(7):
                for j in range(4):
                        if i%3==0 and j not in(0,3) or j==0 and i in(1,2) or j==3 and i in(4,5):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_s():
        """ Pattern of Small Alphabet: 's' using while loop """
        i=0
        while i<7:
                j=0
                while j<4:
                        if i%3==0 and j not in(0,3) or j==0 and i in(1,2) or j==3 and i in(4,5):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
