n=int(input())
l,s=len(str(n))-1,0
while(n!=0):
    r=n//(10**l)
    s+=r**2
    n=n%(10**l)
    l-=1
    if(n==0 and s>9):
        n=s
        s=0
        l=len(str(n))-1
if(s==1 or n==7):
    print(True)
else:
    print(False)