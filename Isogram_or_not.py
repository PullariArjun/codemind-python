n=input()
if(len(n)==len(list(set(n)))):
    print(True)
else:
    print(False)