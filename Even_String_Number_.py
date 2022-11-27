a=input()
z=[int(i) for i in a if(i.isdigit())]
k=[i for i in z if i%2==0]
if(len(k)):
    a=min(k)
    z=list(set(z))
    z.remove(a)
    z.sort(reverse=True)
    for i in z:
        print(i,end="")
    print(a)
else:
    print('-1')