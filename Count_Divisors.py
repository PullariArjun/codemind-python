i,r,k=map(int,input().split())
count=0
for x in range(i,r+1):
    if(x%k==0):
        count+=1
print(count)