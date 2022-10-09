t=int(input())
for z in range(t):
    n,m=map(int,input().split())
    arr1=[int(i) for i in input().split()]
    arr2=[int(i) for i in input().split()]
    arr3=[]
    for i in range(n):
        arr3.append(arr1[i])
    for i in range(m):
        arr3.append(arr2[i])
    print(*sorted(arr3))