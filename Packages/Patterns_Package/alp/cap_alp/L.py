def for_L():
        """ Pattern of Captital Alphabet: 'L' using for loop"""
        for i in range(7):
                for j in range(4):
                        if i==6 or j==0:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_L():
        """ Pattern of Captital Alphabet: 'L' using while loop"""
        i=0
        while i<7:
                j=0
                while j<4:
                        if i==6 or j==0:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
