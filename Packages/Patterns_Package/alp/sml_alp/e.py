def for_e():
        """ Pattern of Small Alphabet: 'e' using for loop"""
        for i in range(5):
                for j in range(5):
                        if i%4==0 and j not in(0,4) or j==0 and i in(1,2,3) or i==2 and j>1 or i==1 and j==4:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_e():
        """ Pattern of Small Alphabet: 'e' using while loop"""
        i=0
        while i<5:
                j=0
                while j<5:
                        if i%4==0 and j not in(0,4) or j==0 and i in(1,2,3) or i==2 and j>1 or i==1 and j==4:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
