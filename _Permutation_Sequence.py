from itertools import *
a,b=map(int,input().split())
lst=list(permutations(list(range(1,a+1))))
a=list(lst[b-1])
for i in a:
    print(i,end="")