n=int(input())
arr=[int(i) for i in input().split()]
a=[]
for i in arr:
    a.append(i*i)
print(*(sorted(a)))