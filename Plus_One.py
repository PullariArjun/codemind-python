n=int(input())
lst=list(map(str,input().split()))
a=''
for i in lst:
    a+=i
a=str(int(a)+1)
for i in a:
    print(i,end=" ")