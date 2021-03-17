def for_w():
        """ Pattern of Small Alphabet: 'W' using for loop """
        for i in range(5):
                for j in range(17):
                        if i==j or i+j==8 or j-i==8 or i+j==16:
                                print('*',end='')
                        else:
                                print(' ',end='')
                print()
def while_w():
        """ Pattern of Small Alphabet: 'W' using while loop """
        i=0
        while i<5:
                j=0
                while j<17:
                        if i==j or i+j==8 or j-i==8 or i+j==16:
                                print('*',end='')
                        else:
                                print(' ',end='')
                        j+=1
                i+=1
                print()
