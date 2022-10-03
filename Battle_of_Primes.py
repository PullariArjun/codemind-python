def pr(n):
    count=0
    for i in range(2,n//2+1):
        if(n%i==0):
            count+=1
    return count
a=int(input())
b=int(input())
for i in range(a+b+1,9999):
    if(pr(i)==0):
        print(i-a-b)
        break