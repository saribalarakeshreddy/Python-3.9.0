def for_v():
        """ Pattern of Small Alphabet: 'v' using for loop"""
        for i in range(5):
                for j in range(9):
                        if i==j or i+j==8:
                                print('*',end='')
                        else:
                                print(' ',end='')
                print()
def while_v():
        """ Pattern of Small Alphabet: 'v' using while loop"""
        i=0
        while i<5:
                j=0
                while j<9:
                        if i==j or i+j==8:
                                print('*',end='')
                        else:
                                print(' ',end='')
                        j+=1
                i+=1
                print()
