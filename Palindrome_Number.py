def pali(n):
    s=0
    while(n):
        r=n%10
        s=s*10+r
        n=n//10
    return s
t=int(input())
for i in range(t):
    n=int(input())
    if(n==pali(n)):
        print(True)
    else:
        print(False)