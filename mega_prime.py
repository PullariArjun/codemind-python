import math
def prime(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    if(count==2):
        return True
    else:
        return False
n=int(input())
c=int(math.log10(n))+1
count=0
if(prime(n)):
    while(n):
        r=n%10
        if(prime(r)):
            count+=1
        n=n//10
    if(count==c):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")