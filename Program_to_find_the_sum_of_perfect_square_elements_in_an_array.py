def sqr(n):
    z=0
    for i in range(0,n+1):
        if(i*i==n):
            z=1
    return z
n=int(input())
s=0
arr=[int(i) for i in input().split()]
for i in arr:
    if(sqr(i)==1):
        s+=i
print(s)