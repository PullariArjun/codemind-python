s=input().split()
ma=mi=0
for i in s:
    mi+=ord(min(i))
    ma+=ord(max(i))
print(abs(ma-mi))