def for_B():
        """ Pattern of Captital Alphabet: 'B' using for loop"""
        for i in range(7):
                for j in range(4):
                        if i%3==0 and j<3 or j==0 or j==3 and i%3!=0:
                                print('*', end=' ')
                        else:
                                print(' ',end=' ')
                print()

def while_B():
        """ Pattern of Captital Alphabet: 'B' using while loop"""
        i=0
        while i<7:
                j=0
                while j<4:
                        if i%3==0 and j<3 or j==0 or j==3 and i%3!=0:
                                print('*', end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
