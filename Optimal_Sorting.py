n=int(input())
for _ in range(n):
    a=int(input())
    lst=[int(i) for i in input().split()]
    if(lst==sorted(lst)):
        print("0")
    else:
        print(max(lst)-min(lst))