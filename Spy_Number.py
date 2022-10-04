n=int(input())
s,p=0,1
while(n):
    r=n%10
    s+=r
    p*=r
    n=n//10
if(s==p):
    print("Spy Number")
else:
    print("Not Spy Number")