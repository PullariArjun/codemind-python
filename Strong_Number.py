def fac(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p
n=int(input())
temp=n
s=0
while(n):
    r=n%10
    s+=fac(r)
    n=n//10
if(temp==s):
    print("The number",temp,"is a strong number")
else:
    print("The number",temp,"is not a strong number")