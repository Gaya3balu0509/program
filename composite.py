num=int(input())
flag=0
for i in range(2,num):
    if num%i==0:
      flag=1
      break
if flag==1:
    print("yes")
else:
    print("no")
