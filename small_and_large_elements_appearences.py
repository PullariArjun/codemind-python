n=input()
s=''
for i in n:
    if i.isdigit() or i.isalpha():
        s+=i
print(min(s),s.count(min(s)),max(s),s.count(max(s)))