def for_u():
        """ Pattern of Small Alphabet: 'u' using for loop """
        for i in range(5):
                for j in range(5):
                        if j%4==0 and i<4 or i==4 and j!=0:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_u():
        """ Pattern of Small Alphabet: 'u' using while loop """
        i=0
        while i<5:
                j=0
                while j<5:
                        if j%4==0 and i<4 or i==4 and j!=0:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
