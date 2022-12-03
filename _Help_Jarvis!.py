for _ in range(int(input())):
    a=input()
    lst=[int(i) for i in a]
    lst=sorted(lst)
    for i in range(len(lst)-1):
        if(lst[i+1]-lst[i]!=1):
            print("NO")
            break
    else:
        print("YES")