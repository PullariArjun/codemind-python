n=int(input())
l=0
while(n):
    r=n%10
    if(l<r):
        l=r
    n=n//10
print(l)