n=int(input())
p,s=1,0
while(n):
    r=n%10
    p*=r
    s+=r
    n=n//10
print(p-s)