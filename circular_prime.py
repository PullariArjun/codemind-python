def prime(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    return count
def rev(n):
    s=0
    while(n):
        r=n%10
        s=s*10+r
        n=n//10
    return s
n=int(input())
if(prime(n)==2):
    if(prime(rev(n))==2):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")