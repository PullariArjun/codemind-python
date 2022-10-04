n=int(input())
ev,od=0,0
while(n):
    r=n%10
    if(r%2==0):
        ev+=1
    else:
        od+=1
    n=n//10
if(ev==0 and od!=0):
    print("Odd")
elif(ev!=0 and od==0):
    print("Even")
else:
    print("Mixed")