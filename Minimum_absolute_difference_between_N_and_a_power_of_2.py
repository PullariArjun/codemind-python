n=int(input())
i=s=0
while(s<n):
    s=2**i
    i+=1
if((s-n)>=(n-s//2)):
    print(n-s//2)
else:
    print(s-n)