st=int(input())
s=0
while(st>0):
    n1=st%10
    s=s*10+n1
    st=st//10
print(s)
