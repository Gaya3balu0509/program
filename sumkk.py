a,b=map(int,input().split())
l1=list(map(int,input().split()))
c=0
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]+l1[j]==b:
            c=1
if c==1:        
    print("YES")
else:
    print("NO")
