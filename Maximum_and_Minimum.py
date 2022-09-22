n=int(input())
arr=[int(i) for i in input().split()]
arr1=[]
k=0
for i in range(0,n):
    count=1
    for j in range(0,n):
        if(arr[i]==arr[j] and i!=j):
            arr[j]=0
            count=count+1
    if(count==arr[i]):
        arr1.append(arr[i])
        k+=1
if(k!=0):
    print(min(arr1),max(arr1))
else:
    print("-1")