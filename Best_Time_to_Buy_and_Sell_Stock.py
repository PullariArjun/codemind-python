n=int(input())
arr=[int(i) for i in input().split()]
p=0
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if((arr[j]-arr[i])>p):
            p=arr[j]-arr[i]
print(p)