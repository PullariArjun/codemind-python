n=int(input())
arr=[int(i) for i in input().split()]
for i in range(n):
    for j in range(n-1):
        if(arr[j]==0):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(*arr)