for _ in range(int(input())):
    n=int(input())
    n=input()
    for i in n:
        if(n.count(i)==1):
            print(i)
            break
    else:
        print('-1')