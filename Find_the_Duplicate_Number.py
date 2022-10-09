n=int(input())
arr=[int(i) for i in input().split()]
for i in range(len(arr)):
    count=1
    for j in range(len(arr)):
        if(arr[i]==arr[j] and i!=j):
            count+=1
            arr[j]=-1
    if(count==2):
        print(arr[i])