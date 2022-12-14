n=int(input())
lst=[int(i) for i in input().split()]
for i in range(n):
    if(sum(lst[:i:])+sum(lst[i::])%2==0):
        print(1)
        break
else:
    print(0)