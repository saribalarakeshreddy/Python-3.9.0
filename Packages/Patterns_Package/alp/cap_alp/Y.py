def for_Y():
        """ Pattern of Captital Alphabet: 'Y' using for loop """
        for i in range(8):
                for j in range(8):
                        if i==j and i<4 or i+j==7:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_Y():
        """ Pattern of Captital Alphabet: 'Y' using while loop """
        i=0
        while i<8:
                j=0
                while j<8:
                        if i==j and i<4 or i+j==7:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
