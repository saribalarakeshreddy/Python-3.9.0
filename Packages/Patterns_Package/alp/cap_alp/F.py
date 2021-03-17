def for_F():
        """ Pattern of Captital Alphabet: 'F' using for loop"""
        for i in range(7):
                for j in range(5):
                        if i%3==0 and i<6 or j==0:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_F():
        """ Pattern of Captital Alphabet: 'F' using while loop"""
        i=0
        while i<7:
                j=0
                while j<5:
                        if i%3==0 and i<6 or j==0:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
