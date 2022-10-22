n=input()
v="aeiouAEIOU";
vo,di,sp,co=0,0,0,0
for i in n:
    if(i in v):
        vo+=1
    elif(i.isdigit()):
        di+=1
    elif(i==' '):
        sp+=1
    else:
        co+=1
print("Vowels:",vo)
print("Consonants:",co)
print("Digits:",di)
print("White spaces:",sp)