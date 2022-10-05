def rev(n):
    s=0
    while(n):
        r=n%10
        s=s*10+r
        n=n//10
    return s
n=int(input())
for i in range(n+1,9999):
    if(i==rev(i)):
        fp=i
        break
for i in range(n-1,0,-1):
    if(i==rev(i)):
        sp=i
        break
if((fp-n)>(n-sp)):
    print(sp)
elif((fp-n)<(n-sp)):
    print(fp)
else:
    print(sp,fp)