n=input().split()
vow='aeiouAEIOU'
count=0
for i in n:
    if i[0] in vow and i[len(i)-1] not in vow:
        count+=1
print(count)