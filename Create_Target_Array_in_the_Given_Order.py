a=int(input())
lst=list(map(int,input().split()))
n=int(input())
lst1=list(map(int,input().split()))
a=[]
for i in range(len(lst)):
    a.insert(lst1[i],lst[i])
print(*a)