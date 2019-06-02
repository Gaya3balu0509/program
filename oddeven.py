st=str(input())
flag1,flag2="",""
for i in range(0,len(st)):
    if  i%2==0:
        flag1+=st[i]
    else:
        flag2+=st[i]
print(flag1,end=" ")
print(flag2)
