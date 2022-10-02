from math import *
def sqr(n):
    c=0
    for i in range(0,int(sqrt(n))+2):
        if(i**2==n):
            c=1
    if(c==1):
        return True
    else:
        return False
n=int(input())
z=0
for i in range(1,n+1):
    if(sqr(i)==True and sqr(n-i)==True):
        z=1
if(z==1):
    print("True")
else:
    print("False")
    