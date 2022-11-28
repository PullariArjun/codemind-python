def rev(n):
    x=str(n)
    return int(x[::-1])
n=int(input())
n=n+rev(n)
while(n!=rev(n)):
    n+=rev(n)
print(n)