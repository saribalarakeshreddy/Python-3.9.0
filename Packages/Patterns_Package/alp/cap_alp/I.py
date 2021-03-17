def for_I():
        """ Pattern of Captital Alphabet: 'I' using for loop"""
        for i in range(7):
                for j in range(3):
                        if i%6==0 or j==1:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
def while_I():
        """ Pattern of Captital Alphabet: 'I' using while loop"""
        i=0
        while i<7:
                j=0
                while j<3:
                        if i%6==0 or j==1:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                        j+=1
                i+=1
                print()
                        
