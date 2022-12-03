for _ in range(int(input())):
    n=int(input())
    lst=[int(i) for i in input().split()]
    c=0
    lst=list(set(lst))
    for i in range(n):
        for j in range(n):
            if(i==j):
                continue
            for k in range(n):
                if(lst[i]+lst[j]==lst[k]):
                    c+=1
    if(c!=0):
        print(c//2)
    else:
        print('-1')