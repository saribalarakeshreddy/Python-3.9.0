def for_r():
        """ Pattern of Small Alphabet: 'r' using for loop """
        for i in range(6):
                for j in range(5):
                        if j==0 or i==0 and j in (2,3) or i==1 and j in(1,4) :
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_r():
        """ Pattern of Small Alphabet: 'r' using while loop """
        i=0
        while i<6:
                j=0
                while j<5:
                        if j==0 or i==0 and j in (2,3) or i==1 and j in(1,4) :
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
