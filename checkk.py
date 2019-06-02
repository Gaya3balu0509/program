ls,ls1=map(int,input().split())
list1=list(map(int,input().split()))
c=0
for i in list1:
    if i==ls1:
        c=1
if c==1:
    print("yes")
else:
    print("no")
