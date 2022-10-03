n=int(input())
arr=[int(i) for i in input().split()]
for i in range(arr[0],0,-1):
    count=0
    for j in arr:
        if(j%i==0):
            count+=1
    if(count==len(arr)):
        print(i)
        break