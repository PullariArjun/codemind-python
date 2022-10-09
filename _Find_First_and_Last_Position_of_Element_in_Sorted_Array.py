n=int(input())
arr=[int(i) for i in input().split()]
z=int(input())
for i in range(0,len(arr)):
    if(arr[i]==z):
        print(i,end=" ")
        break
else:
    print("-1",end=" ")
for i in range(len(arr)-1,-1,-1):
    if(arr[i]==z):
        print(i)
        break
else:
    print("-1")