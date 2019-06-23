inp1,inp2=map(str,input().split())
c=0
for i in inp1:
    for j in inp2:
        if i==j:
            c=1
if c==1:        
    print("yes")
else:
    print("no")
