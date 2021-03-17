def for_C():
        """ Pattern of Captital Alphabet: 'C' using for loop"""
        for i in range(5):
                for j in range(4):
                        if i%4==0 and j>0 or j==0 and i not in(0,4):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_C():
    """ Pattern of Captital Alphabet: 'C' using while loop"""
    i=0
    while i<5:
        j=0
        while j<4:
            if i%4==0 and j>0 or j==0 and i not in(0,4):
                print('*',end=' ')
            else:
                print(' ',end=' ')
            j+=1
        i+=1
        print()

