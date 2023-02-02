n=input()
vow='aeiouAEIOU'
a=' '
for i in n:
    if i in vow and a[-1]=='V':
        continue
    elif i not in vow and a[-1]=='C':
        continue
    if i in vow:
        a+='V'
    else:
        a+='C'
print(a[1::])