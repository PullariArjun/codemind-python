n=int(input())
arr=[int(i) for i in input().split()]
s=0
for i in range(len(arr)-1):
    if((arr[i+1]-arr[i])>0):
        s+=arr[i+1]-arr[i]
print(s)