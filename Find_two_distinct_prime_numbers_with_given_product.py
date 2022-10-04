def prime(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    return count
flag=0
n=int(input())
for i in range(2,n):
    if(n%i==0 and prime(i)==2 and prime(n//i)==2):
        print(i,n//i)
        flag=1
        break
if(flag==0):
    print("-1")