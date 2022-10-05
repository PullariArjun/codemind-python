n=int(input())
x=len(str(n))
arr=[]
while(n):
    r=n%10
    if(r not in arr):
        arr.append(r)
    n=n//10
if(x==len(arr)):
    print("Unique Number")
else:
    print("Not Unique Number")