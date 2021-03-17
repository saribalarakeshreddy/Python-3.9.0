def for_t():
        """ Pattern of Small Alphabet: 't' using for loop"""
        for i in range(7):
                for j in range(5):
                        if j==1 and i<6  or i==2 and j<4 or i==6 and j in (2,3) or i==5 and j==4:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_t():
        """ Pattern of Small Alphabet: 't' using while loop"""
        i=0
        while i<7:
                j=0
                while j<5:
                        if j==1 and i<6  or i==2 and j<4 or i==6 and j in (2,3) or i==5 and j==4:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
