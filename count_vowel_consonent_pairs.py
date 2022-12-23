n=input()
l=len(n)
vow,count="aeiouAEIOU",0
for i in range(l//2):
    if(n[i]==" " or n[l-i-1]==" "):
        continue
    if n[i] in vow and n[l-i-1] not in vow or n[i] not in vow and n[l-i-1] in vow:
        count+=1
print(count)