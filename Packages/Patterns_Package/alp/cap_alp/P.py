def for_P():
        """ Pattern of Captital Alphabet: 'P' using for loop"""
        for i in range(8):
                for j in range(5):
                        if j==0 or i%4==0 and j<4 or j==4 and i in(1,2,3):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_P():
        """ Pattern of Captital Alphabet: 'P' using while loop"""
        i=0
        while i<8:
                j=0
                while j<5:
                        if j==0 or i%4==0 and j<4 or j==4 and i in(1,2,3):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
