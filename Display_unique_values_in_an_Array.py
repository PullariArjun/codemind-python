n=int(input())
arr=[int(i) for i in input().split()]
z=0
for i in range(n):
    count=0
    for j in range(n):
        if(arr[i]==arr[j]):
            count+=1
    if(count==1):
        print(arr[i],end=" ")
        z=1
if(z==0):
    print("-1")