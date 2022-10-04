def ps(n):
    c=0
    for i in range(1,n):
        if(i*i==n):
            c+=1
    if(c!=0):
        return True
    else:
        return False
t=int(input())
for i in range(t):
    n=int(input())
    print(ps(n))