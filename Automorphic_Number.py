n=int(input())
d=len(str(n))
sq,i,s=n*n,0,0
while(i!=d):
    r=sq%10
    s=s+r*(10**i)
    sq=sq//10
    i+=1
if(s==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")