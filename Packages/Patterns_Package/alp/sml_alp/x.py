def for_x():
        """ Pattern of Small Alphabet: 'x' using for loop """
        for i in range(5):
                for j in range(5):
                        if i==j or i+j==4:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_x():
        """ Pattern of Small Alphabet: 'x' using while loop """
        i=0
        while i<5:
                j=0
                while j<5:
                        if i==j or i+j==4:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
