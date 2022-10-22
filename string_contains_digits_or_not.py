t=int(input())
for i in range(t):
    n,d=input(),0
    for j in n:
        if(j.isdigit()):
            d+=1
    if(d==0):
        print("No")
    else:
        print("Yes")