n=int(input())
arr=[int(i) for i in input().split()]
count=0
for i in range(1,n-1):
    if((arr[i-1]%2==0 and arr[i+1]%2==1)or(arr[i-1]%2==1 and arr[i+1]%2==0)):
        count+=1
if((arr[n-2]%2==0 and arr[0]%2==1)or(arr[n-2]%2==1 and arr[0]%2==0)):
    count+=1
if((arr[n-1]%2==0 and arr[1]%2==1)or(arr[n-1]%2==1 and arr[1]%2==0)):
    count+=1
print(count)