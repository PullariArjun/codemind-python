n,k=map(int,input().split())
arr=[int(i) for i in input().split()]
c=0
for x in range(len(arr)):
    for y in range(x,len(arr)):
        s=0
        for z in range(x,y+1):
            s+=arr[z]
        if(s==k):
            c+=1
print(c)