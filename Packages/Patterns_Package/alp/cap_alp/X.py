def for_X():
        """ Pattern of Captital Alphabet: 'X' using for loop"""
        for i in range(8):
                for j in range(8):
                        if i==j or i+j==7:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_X():
        """ Pattern of Captital Alphabet: 'X' using while loop"""
        i=0
        while i<8:
                j=0
                while j<8:
                        if i==j or i+j==7:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
