def for_H():
        """ Pattern of Captital Alphabet: 'H' using for loop"""
        for i in range(7):
                for j in range(5):
                        if j%4==0 or i==3:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_H():
        """ Pattern of Captital Alphabet: 'H' using while loop"""
        i=0
        while i<7:
                j=0
                while j<5:
                        if j%4==0 or i==3:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
