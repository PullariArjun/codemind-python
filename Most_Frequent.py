n=int(input())
lst=list(map(int,input().split()))
m=0
for i in lst:
    if(lst.count(i)>m):
        m=lst.count(i)
a=[i for i in lst if lst.count(i)==m]
print(min(a))