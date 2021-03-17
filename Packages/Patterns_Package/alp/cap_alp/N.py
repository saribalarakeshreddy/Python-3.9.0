def for_N():
        """ Pattern of Captital Alphabet: 'N' using for loop"""
        for i in range(6):
                for j in range(8):
                        if j%7==0 or j-i==1:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_N():
                """ Pattern of Captital Alphabet: 'N' using while loop"""
                i=0
                while i<6:
                        j=0
                        while j<8:
                                if j%7==0 or j-i==1:
                                        print('*',end=' ')
                                else:
                                        print(' ',end=' ')
                                j+=1
                        i+=1
                        print()
