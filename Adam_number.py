def rev(n):
    s=0
    while(n):
        r=n%10
        s=s*10+r
        n=n//10
    return s
n=int(input())
if(n*n==rev(rev(n)*rev(n))):
    print(True)
else:
    print(False)