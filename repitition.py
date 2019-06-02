ls,ls1=map(int,input().split())
list1=list(map(int,input().split()))
max1=1
for i in list1:
    if list1.count(i)>max1:
        max1=list1.count(i)
print(max1)
