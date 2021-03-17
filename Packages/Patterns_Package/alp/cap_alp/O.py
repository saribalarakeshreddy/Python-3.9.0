def for_O():
        """ Pattern of Captital Alphabet: 'O' using for loop """
        for i in range(7):
                for j in range(5):
                        if j%4==0 and i not in (0,1,5,6) or (i==1 or i==5) and j not  in (0,4):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_O():
        """ Pattern of Captital Alphabet: 'O' using while loop """
        i=0
        while i<7:
                j=0
                while j<5:
                        if j%4==0 and i not in (0,1,5,6) or (i==1 or i==5) and j not  in (0,4):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
