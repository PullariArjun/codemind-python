a=[int(i)for i in input().split()]
b=[int(i)for i in input().split()]
al,bo=0,0
for i in range(len(a)):
    if(a[i]>b[i]):
        al+=1
    elif(a[i]<b[i]):
        bo+=1
print(al,bo)