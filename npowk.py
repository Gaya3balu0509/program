inp1,inp2=map(int,input().split())
flag=0
for i in  range(1,inp1):
    if inp2**i==inp1:
        flag=1
        break
if flag==1:
    print("yes")
else:
    print("no")
