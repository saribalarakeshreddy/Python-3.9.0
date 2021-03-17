def for_Reverse_Left_faced_Right_Angled_Triangle():
    """ pattern for : Reverse_Left_faced_Right_Angled_Triangle"""
    for i in range(5):
        for j in range(5):
            if i<=j:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
def while_Reverse_Left_faced_Right_Angled_Triangle():
    """ pattern for : Reverse_Left_faced_Right_Angled_Triangle"""
    i=0
    while i<5:
        j=0
        while j<5:
            if i<=j:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            j+=1
        i+=1
        print()