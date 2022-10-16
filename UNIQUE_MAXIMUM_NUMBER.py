n=int(input())
arr=[int(i) for i in input().split()]
a=[]
for i in range(0,n):
    c=0
    for j in range(0,n):
        if(arr[i]==arr[j]):
            c+=1
    if(c==1):
        a.append(arr[i])
if(len(a)!=0):
    print(max(a))
else:
    print("-1")