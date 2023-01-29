n=input().lower().split()
flag=0
for i in n[0]:
    for j in n:
        if(i not in j):
            break
    else:
        print(i,end="")
        flag=1
if(flag==0):
    print("-1")