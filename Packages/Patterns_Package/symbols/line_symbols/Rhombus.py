def for_Rhombus():
    """ pattern for : Diamond_or_Rhombus uing for loop"""
    for  i in range(7):
        for j in range(7):
            if i+j==9 or i-j==3 or i+j==3 or j-i==3:
                print('*', end=' ')
            else:
                print(' ',end=' ')
        print()
def while_Rhombus():
    """ pattern for : Diamond_or_Rhombus using while loop"""
    i=0
    while i<7:
        j=0
        while j<7:
            if i+j==9 or i-j==3 or i+j==3 or j-i==3:
                print('*', end=' ')
            else:
                print(' ',end=' ')
            j+=1
        i+=1
        print()