def for_o():
        """ Pattern of Small Alphabet: 'o' using for loop"""
        for i in range(4):
                for j in range(4):
                        if i in (0,3) and j not in(0,3) or j in(0,3) and i not in(0,3):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_o():
        """ Pattern of Small Alphabet: 'o' using while loop"""
        i=0
        while i<4:
                j=0
                while j<4:
                        if i in (0,3) and j not in(0,3) or j in(0,3) and i not in(0,3):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
