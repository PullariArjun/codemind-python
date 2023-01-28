s=input().split()
s=s[len(s)-1]
if(min(s).lower() in s):
    print(min(s).lower())
else:
    print(min(s))