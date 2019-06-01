str1=input()
s=[]
for i in str1:
    if i.isdigit():
        s.append(i)
if s==[]:
    print()
else:
    for i in s:
        print(i,end='')
