def for_W():
        """ Pattern of Captital Alphabet: 'W' using for loop"""
        for i in range(8):
                for j in range(32):
                        if i==j or i+j==14 or j-i==14 or i+j==28:
                                print('*',end='')
                        else:
                                print(' ',end='')
                print()
def while_W():
        """ Pattern of Captital Alphabet: 'W' using while loop"""
        i=0
        while i<8:
                j=0
                while j<32:
                        if i==j or i+j==14 or j-i==14 or i+j==28:
                                print('*',end='')
                        else:
                                print(' ',end='')
                        j+=1
                i+=1
                print()
