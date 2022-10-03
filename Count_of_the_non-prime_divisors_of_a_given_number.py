def p(n):
    count=0
    if n==1:
        return 2
    for i in range(2,n):
        if(n%i==0):
            count+=1
    return count
n=int(input())
count=0
for i in range(1,n+1):
    if(n%i==0 and p(i)!=0):
        count+=1
print(count)