n=int(input())
arr=[int(i) for i in input().split()]
x=1
for i in arr:
    x*=i
for i in range(arr[0],x+1):
    count=0
    for j in arr:
        if(i%j==0):
            count+=1
    if(count==len(arr)):
        print(i)
        break