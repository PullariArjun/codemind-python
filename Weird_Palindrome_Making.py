for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    a=[i for i in lst if i%2]
    print(len(a)//2)