def for_D():
        """ Pattern of Captital Alphabet: 'D' using for loop """
        for i in range(5):
                for j in range(5):
                        if i==0 and j!=4 or j==0 or i==4 and j!=4 or j==4 and i not in(0,4):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_D():
    """ Pattern of Captital Alphabet: 'D' using while loop"""
    i=0
    while i<5:
        j=0
        while j<5:
            if i==0 and j!=4 or j==0 or i==4 and j!=4 or j==4 and i not in(0,4):
                print('*',end=' ')
            else:
                print(' ',end=' ')
            j+=1
        i+=1
        print()

