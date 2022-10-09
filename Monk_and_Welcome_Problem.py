n=int(input())
arr1=[int(i) for i in input().split()]
arr2=[int(i) for i in input().split()]
for i in range(len(arr1)):
    print(arr1[i]+arr2[i],end=" ")