def for_Zero():
        """ Pattern of Number : '0' using for loop"""
        for i in range(7):
                for j in range(5):
                        if i in (0,6) and j not in(0,4) or j in(0,4) and i not in(0,6) or i+j==5:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_Zero():
        """ Pattern of Number : '0' using while loop"""
        i=0
        while i<7:
                j=0
                while j<5:
                        if i in (0,6) and j not in(0,4) or j in(0,4) and i not in(0,6) or i+j==5:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
