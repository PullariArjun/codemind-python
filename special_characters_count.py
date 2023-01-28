s,count=input(),0
for i in s:
    if(i.isdigit()==False and i.isalpha()==False and i.isspace()==False):
        count+=1
print(count)