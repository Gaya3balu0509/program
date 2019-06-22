inp1,inp2=map(str,input().split())
list1=list(map(int,input().split()))
c=0
for i in list1:
    if i==int(inp2):
        c=1
if c==1:    
     print("Yes")
else:
    print("No")
