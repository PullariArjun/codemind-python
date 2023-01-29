n=input().lower().split()
count=0
for i in n[0]:
    for j in n:
        if(i not in j):
            break
    else:
        count+=1
print(count)