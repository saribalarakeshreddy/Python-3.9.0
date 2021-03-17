def for_d():
        """ Pattern of Small Alphabet: 'd' using for loop """
        for i in range(7):
                for j in range(5):
                        if j==4 or i%3==0 and i>0 and j>0 or j==0 and i in (4,5):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_d():
        """ Pattern of Small Alphabet: 'd' using while loop """
        i=0
        while i<7:
                j=0
                while j<5:
                        if j==4 or i%3==0 and i>0 and j>0 or j==0 and i in (4,5):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
                
