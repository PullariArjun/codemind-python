n=int(input())
arr=[int(i) for i in input().split()]
count,m=0,0
for i in range(len(arr)):
    if(arr[i]==1):
        count+=1
    if(arr[i]==0 or i==len(arr)-1):
        if(count>m):
            m=count
        count=0
print(m)