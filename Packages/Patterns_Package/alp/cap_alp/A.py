def for_A():
        """ Pattern of Captital Alphabet: 'A'  using for loop"""
        for i in range(9):
                for j in range(9):
                        if i+j==4 or j-i==4 or i==2 and j in range(2,7):
                                print('*', end='')
                        else:
                                print(' ', end='')
                print()

def while_A():
        """ Pattern of Captital Alphabet: 'A'  using while loop"""
        i=0
        while i<9:
                j=0
                while j<9:
                        if i+j==4 or j-i==4 or i==2 and j in range(2,7):
                                print('*', end='')
                        else:
                                print(' ', end='')
                        j+=1
                i+=1
                print()

