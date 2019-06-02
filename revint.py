st=int(input())
s=0
while(st>0):
    nn=st%10
    s=s*10+nn
    st=st//10
print(s)
