n=input()
for i in range(len(n)):
    for j in range(len(n)):
        if(n[i]==n[j] and i!=j):
            break
    else:
        print(i)
        break
else:
    print("-1")