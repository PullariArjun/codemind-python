n=int(input())
s=0
for i in range(2,n//2):
    if(i*(i+1)==n):
        s=1
if(s==1):
    print("YES")
else:
    print("NO")