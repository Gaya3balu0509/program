str1=input()
c,d=0,0
for i in str1:
    if  i.isalpha():
        d=d+1
    elif i.isdigit():
        c=c+1
if c>1 and d>1:
    print("Yes")
else:
    print("No")
