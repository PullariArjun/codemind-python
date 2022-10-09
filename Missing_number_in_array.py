t=int(input())
for z in range(t):
    n=int(input())
    arr=[int(i)for i in input().split()]
    for i in range(1,len(arr)+2):
        if(i not in arr):
            print(i)
            break