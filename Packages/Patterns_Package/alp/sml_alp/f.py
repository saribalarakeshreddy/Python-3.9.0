def for_f():
        """ Pattern of Small Alphabet: 'f' using for loop"""
        for i in range(8):
                for j in range(5):
                        if j==1 and i>0 or i==0 and j in(2,3) or i==1 and j==4 or i==4 and j<4:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_f():
        """ Pattern of Small Alphabet: 'f' using while loop"""
        i=0
        while i<8:
                j=0
                while j<5:
                        if j==1 and i>0 or i==0 and j in(2,3) or i==1 and j==4 or i==4 and j<4:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
