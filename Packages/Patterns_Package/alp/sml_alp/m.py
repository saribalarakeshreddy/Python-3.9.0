def for_m():
        """ Pattern of Small Alphabet: 'm' using for loop """
        for i in range(7):
                for j in range(10):
                        if j%3==0 and j>0 and i>1 or i==0 and j in(1,2) or i==1 and j%3!=0 and j>2 or j==3 and i>0 or i==1 and j==0:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_m():
        """ Pattern of Small Alphabet: 'm' using while loop """
        i=0
        while i<7:
                j=0
                while j<10:
                        if j%3==0 and j>0 and i>1 or i==0 and j in(1,2) or i==1 and j%3!=0 and j>2 or j==3 and i>0 or i==1 and j==0:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
