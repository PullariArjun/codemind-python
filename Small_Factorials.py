for i in range(int(input())):
    n=int(input())
    fac=1
    for j in range(1,n+1):
        fac*=j
    print(fac)