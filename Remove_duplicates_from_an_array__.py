n=int(input())
arr=[int(i)for i in input().split()]
arr1=[]
for i in arr:
    if(i not in arr1):
        arr1.append(i)
print(*arr1)