def for_Triangle_Piece_Taken_out_from_a_Rectangle():
    """ pattern for :Triangle_Piece_Taken_out_from_a_Rectangle using for loop"""
    for i in range(5):
        for j in range(7):
            if i+j<=3 or j-i>=3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
    for i  in range(4):
        for j in range(7):
            if i+j>=3 and  j-i<=3:
                print('*',end=' ')
            else:
                print(' ', end=' ')
        print()
def while_Triangle_Piece_Taken_out_from_a_Rectangle():
    """ pattern for :Triangle_Piece_Taken_out_from_a_Rectangle using while loop"""
    i=0
    while i<5:
        j=0
        while j<7:
            if i+j<=3 or j-i>=3:
                print('*',end=' ')
            else:
                print(' ',end=' ')
            j+=1
        i+=1
        print()
    i=0
    while i<4:
        j=0
        while j<7:
            if i+j>=3 and  j-i<=3:
                print('*',end=' ')
            else:
                print(' ', end=' ')
            j+=1
        i+=1
        print()