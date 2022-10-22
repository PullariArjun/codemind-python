t=int(input())
for x in range(t):
    a,d=input(),0
    for i in a:
        if(i.isdigit()):
            d+=1
    if(d==len(a)):
        print(True)
    else:
        print(False)