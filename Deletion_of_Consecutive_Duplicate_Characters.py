for k in range(int(input())):
    a=input()
    z=''
    for i in range(len(a)-1):
        if(a[i]!=a[i+1]):
            z+=a[i]
    print(len(a)-len(z)-1)
    
