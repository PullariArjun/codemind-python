n=int(input())
arr=list(map(int,input().split()))
for i in range(len(arr)):
    c=0
    for j in range(i,len(arr)):
        if(arr[i]>=arr[j]):
            c+=1
        else:
            print(c,end=" ")
            break
        if(j==n-1):
            print("0",end=" ")