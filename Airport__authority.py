n=int(input())
arr=[]
for i in range(0,n):
    x=int(input())
    arr.append(x)
t=int(input())
s=0
for i in arr:
    if(i<=t):
        s+=1
    else:
        s+=2
print(s)