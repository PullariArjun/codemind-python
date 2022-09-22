n=int(input())
arr=[int(i) for i in input().split()]
for i in range(0,n):
    for j in range(0,n):
        if(arr[i]==arr[j] and i!=j):
            arr[j]=(-1)
for i in range(0,n):
    if(arr[i]==(-1)):
        continue
    else:
        print(arr[i],end=" ")