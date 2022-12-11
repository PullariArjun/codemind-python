import itertools as it
l=input()
l=list(l)
a=it.permutations(l)
b=[]
for i in a:
    b.append(list(i))
for i in b:
    for j in i:
        print(j,end='')
    print()