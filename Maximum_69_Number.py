import math
n=int(input())
x=int(math.log10(n))
f=0
while(n):
    r=n//(10**x)
    if(r==6 and f==0):
        r=9
        f=1
    n=n%(10**x)
    x-=1
    print(r,end="")