for _ in range(int(input())):
    n,s=map(int,input().split())
    lst=list(map(int,input().split()))
    x=0
    for i in range(n):
        for j in range(i,n):
            sm=0
            for k in range(i,j+1):
                sm+=lst[k]
            if(sm==s):
                print(i+1,j+1)
                x=1
                break
        if(x==1):
            break
    else:
        print('-1')