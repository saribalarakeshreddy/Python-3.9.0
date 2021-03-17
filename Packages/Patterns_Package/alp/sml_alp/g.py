def for_g():
        """ Pattern of Small Alphabet: 'g' using for loop"""
        for i in range(7):
                for j in range(5):
                        if i%3==0 and j in(1,2,3) or j==0 and i in(1,2,5) or j==4 and i<6:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_g():
        """ Pattern of Small Alphabet: 'g' using while loop"""
        i=0
        while i<7:
                j=0
                while j<5:
                        if i%3==0 and j in(1,2,3) or j==0 and i in(1,2,5) or j==4 and i<6:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
