def for_U():
        """ Pattern of Captital Alphabet: 'U' using for loop """
        for i in range(6):
                for j in range(5):
                        if j in (0,4) and i<5 or i==5 and j not in(0,4):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_U():
        """ Pattern of Captital Alphabet: 'U' using while loop """
        i=0
        while i<6:
                j=0
                while j<5:
                        if j in (0,4) and i<5 or i==5 and j not in(0,4):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
