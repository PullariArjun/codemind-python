def sdn(n):
    temp=n
    while(n):
        r=n%10
        if(r==0):
            return False
        if(temp%r!=0):
            return False
        n=n//10
    else:
        return True
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(sdn(i)):
        print(i,end=" ")