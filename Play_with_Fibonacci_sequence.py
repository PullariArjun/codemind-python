n=int(input())
i,j=0,1
print(i,j,end=" ")
x=2
while(x<n):
    s=i+j
    i=j
    j=s
    print(s,end=" ")
    x+=1