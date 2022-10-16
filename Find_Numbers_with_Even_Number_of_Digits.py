n=int(input())
arr=[int(i) for i in input().split()]
c=0
for i in arr:
    if(len(str(i))%2==0):
        c+=1
print(c)