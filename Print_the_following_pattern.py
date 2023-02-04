n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end='')
    for j in range(65,65+i):
        print(chr(j),end='')
    for j in range(65+i-2,64,-1):
        print(chr(j),end='')
    print()