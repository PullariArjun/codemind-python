n=int(input())
l=[int(i) for i in input().split()]
ev,od=0,0
for i in l:
    if(i%2==0):
        ev+=1
    else:
        od+=1
print(ev,od)