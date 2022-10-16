n=int(input())
arr=[int(i) for i in input().split()]
a,b=0,0
for i in range(0,n):
    if(i%2==0):
        a+=arr[i]
    else:
        b+=arr[i]
if(abs(a-b)==0):
    print("YES")
else:
    print("NO")