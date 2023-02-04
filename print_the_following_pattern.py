n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end='')
    for j in range(1,(n*2)-((n-i)*2)):
        print(i,end='')
    print()