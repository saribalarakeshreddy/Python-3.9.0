def for_Dynamic_Right_faced_Equilataral_Triangle():
    """ pattern for :Dynamic_Right_faced_Equilataral_Triangle using for loop"""
    n=int(input('enter any num'))
    if n%2==0:
        h=int(n/2)
        for i in range(h+1):
            print('*'*i)
        for j in range(len(range(h,n+1)),0,-1):
            print('*'*j)
    else:
        h=int(n//2)+1
        for i in range(h):
            print('*'*i)
        for j in range(len(range(h,n+1)),0,-1):
            print('*'*j)
def while_Dynamic_Right_faced_Equilataral_Triangle():
    """ pattern for :Dynamic_Right_faced_Equilataral_Triangle using while loop"""
    n=int(input('enter any num'))
    if n%2==0:
        h=int(n/2)
        i=0
        while i<h+1:
            print('*'*i)
            i+=1
        j=len(range(h,n+1))
        while j>0:
            print('*'*j)
            j-=1
    else:
        h=int(n//2)+1
        i=0
        while i<h+1:
            print('*'*i)
            i+=1
        j=len(range(h,n+1))
        while j>0:
            print('*'*j)
            j-=1
