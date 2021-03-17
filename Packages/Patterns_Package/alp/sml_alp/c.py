def for_c():
        """ Pattern of Small Alphabet: 'c' using for loop """
        for i in range(4):
                for j in range(4):
                        if i%3==0 and j>0 or j==0 and i in(1,2):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_c():
        """ Pattern of Small Alphabet: 'c' using while loop """
        i=0
        while i<4:
                j=0
                while j<4:
                        if i%3==0 and j>0 or j==0 and i in(1,2):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
