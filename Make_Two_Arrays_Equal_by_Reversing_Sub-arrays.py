n=int(input())
lst1=map(int,input().split())
m=int(input())
lst2=list(map(int,input().split()))
if(sorted(lst1)==sorted(lst2)):
    print(True)
else:
    print(False)