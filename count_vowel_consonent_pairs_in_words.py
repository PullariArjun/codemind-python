s=input().split()
vow,count='AEIOUaeiou',0
for i in s:
    n=len(i)
    for j in range(n//2):
        if i[j] in vow and i[n-1-j] not in vow or i[j] not in vow and i[n-1-j] in vow:
            count+=1
print(count)