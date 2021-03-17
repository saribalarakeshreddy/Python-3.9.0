def for_Reverse_Iscoseles_Triangle_and_With_its_water_image():
    """ pattern for :Reverse_Iscoseles_Triangle_and_With_its_water_image using for loop"""
    for i in range(5):
        for j in range(5):
            if i<=j:
                print('*',end=' ')
            else:
                print('',end=' ')
        print()
    for i  in range(6):
        if i%2==0:
            print((' *'*i).center(10))
        else:
            print((' *'*i).center(10))
def while_Reverse_Iscoseles_Triangle_and_With_its_water_image():
    """ pattern for :Reverse_Iscoseles_Triangle_and_With_its_water_image using while loop"""
    i=0
    while i<5:
        j=0
        while j<5:
            if i<=j:
                print('*',end=' ')
            else:
                print('',end=' ')
            j+=1
        i+=1
        print()
    i=0
    while i<6:
        if i%2==0:
            print((' *'*i).center(10))
        else:
            print((' *'*i).center(10))
        i+=1

