n=int(input())
arr=[int(i) for i in input().split()]
p=0
for i in range(n):
    count=1
    if(arr[i]==(-1)):
        continue
    for j in range(n):
        if(arr[i]==arr[j]and i!=j):
            count+=1
            arr[j]=(-1)
    p+=count//2
print(p)