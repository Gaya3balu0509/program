num=int(input())
c=0
for i in range(0,num+1):
  if i%num==0:
    c=c+1
if c==2:
  print("yes")
else:
  print("no")
