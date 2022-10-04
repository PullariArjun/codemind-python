import math
n=int(input())
temp,s=n,0
x=int(math.log10(n))+1
while(n):
    r=n%10
    s=s+r**x
    x-=1
    n=n//10
if(temp==s):
    print(True)
else:
    print(False)