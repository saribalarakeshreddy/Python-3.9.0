def for_Right_faced_Right_Angled_Triangle():
    """ pattern for : Right_faced_Right_Angled_Triangle using for loop"""
    for i in range(5):
        for j in range(5):
            if i>=j:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
def while_Right_faced_Right_Angled_Triangle():
    """ pattern for : Right_faced_Right_Angled_Triangle using for loop"""
    i=0
    while i<5:
        j=0
        while j<5:
            if i>=j:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            j+=1
        i+=1
        print()