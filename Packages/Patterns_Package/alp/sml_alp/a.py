def for_a():
        """ Pattern of Small Alphabet: 'a' using for loop"""
        for i in range(7):
                for j in range(5):
                        if j==4 and i>0 or j==0 and i in (1,4,5) or i%3==0 and j not in(0,4):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_a():
        """ Pattern of Small Alphabet: 'a' using while loop"""
        i=0
        while i<7:
                j=0
                while j<5:
                        if j==4 and i>0 or j==0 and i in (1,4,5) or i%3==0 and j not in(0,4):
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
