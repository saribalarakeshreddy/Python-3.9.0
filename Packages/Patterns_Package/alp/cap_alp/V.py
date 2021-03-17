def for_V():
        """ Pattern of Captital Alphabet: 'V' using for loop"""
        for i in range(8):
                for j in range(16):
                        if i==j or i+j==14 :
                                print('*',end='')
                        else:
                                print(' ',end='')
                print()
                        
def while_V():
        """ Pattern of Captital Alphabet: 'V' using while loop"""
        i=0
        while i<8:
                j=0
                while j<16:
                        if i==j or i+j==14 :
                                print('*',end='')
                        else:
                                print(' ',end='')
                        j+=1
                i+=1
                print()
