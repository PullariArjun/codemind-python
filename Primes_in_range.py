import math
def p(n):
    if(n==1):
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if(n%i==0):
                return False
        else:
            return True
n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    if(p(i)):
        c+=1
print(c)