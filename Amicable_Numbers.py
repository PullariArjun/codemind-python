def an(n):
    s=0
    for i in range(1,n//2+1):
        if(n%i==0):
            s+=i
    return s
m=int(input())
n=int(input())
if(n==an(m) and m==an(n)):
    print("Amicable")
else:
    print("Not Amicable")