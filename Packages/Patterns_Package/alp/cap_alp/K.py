def for_K():
        """ Pattern of Captital Alphabet: 'K' using for loop """
        for i in range(7):
                for j in range(6):
                        if j==0 or i+j==4 or i-j==2:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_K():
        """ Pattern of Captital Alphabet: 'K' using while loop """
        i=0
        while i<7:
                j=0
                while j<6:
                        if j==0 or i+j==4 or i-j==2:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()

