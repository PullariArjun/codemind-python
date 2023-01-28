s=input().split()
vow='aeiouAEIOU'
min_count=100
for i in s:
    count=0
    for j in i:
        if(j in vow):
            count+=1
    if(min_count>count):
        min_count=count
cnt=0
for i in s:
    count=0
    for j in i:
        if j in vow:
            count+=1
    if(count==min_count):
        cnt+=1
print(cnt)