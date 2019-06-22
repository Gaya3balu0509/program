inp1=input()
o,c=0,0
for i in inp1:
    if i=='(':
        o+=1
    elif i==')':
        c+=1
if c==o:    
     print("yes")
else:
    print("no")
