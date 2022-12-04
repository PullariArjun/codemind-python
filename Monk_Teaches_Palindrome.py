for i in range(int(input())):
    a=input()
    if(a!=a[::-1]):
        print("NO")
    else:
        if(len(a)%2):
            print('YES ODD')
        else:
            print('YES EVEN')