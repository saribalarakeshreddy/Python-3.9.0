def for_Isosceles_Triangle():
    """ pattern for : Isosceles_Triangle using for loop"""
    n=int(input('enter n value:  '))
    for i in range(n):
        s='* '*i
        if i%2==0:
            print(('* '*i).center(n*2))
        else:
            print(s.center(n*2))
def while_Isosceles_Triangle():
    """ pattern for : Isosceles_Triangle using for loop"""
    n=int(input('enter n value:  '))
    i=0
    while i<n:
        s='* '*i
        if i%2==0:
            print(('* '*i).center(n*2))
        else:
            print(s.center(n*2))
        i+=1
