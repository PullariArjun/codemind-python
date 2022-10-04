n=int(input())
i,j,x,s=0,1,2,0
print(i,j,end=" ")
while(x<n):
    s=i+j
    i=j
    j=s
    print(s,end=" ")
    x+=1