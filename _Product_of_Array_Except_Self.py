n=int(input())
arr=[int(i) for i in input().split()]
for i in range(len(arr)):
    p=1
    for j in range(len(arr)):
        if(i!=j):
            p*=arr[j]
    print(p,end=" ")