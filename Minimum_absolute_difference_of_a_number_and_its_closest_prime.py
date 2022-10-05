def prime(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    if(count==2):
        return True
    else:
        return False
n=int(input())
for i in range(n,9999):
    if(prime(i)):
        fp=i
        break
for i in range(n,1,-1):
    if(prime(i)):
        sp=i
        break
if((fp-n)>=(n-sp)):
    print(n-sp)
else:
    print(fp-n)