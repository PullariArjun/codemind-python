n=int(input())
lst=[int(i) for i in input().split()]
while (len(lst)):
    print(len(lst))
    m=min(lst)
    while m in lst:
        lst.remove(m)