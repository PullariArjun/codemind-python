n=int(input())
arr=[int(i) for i in input().split()]
m=0
for i in range(n):
    count=0
    for j in range(n):
        if(arr[i]==arr[j]):
            count+=1
    if(count>m):
        m=count
        e=arr[i]
print(e)