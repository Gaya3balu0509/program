num1=int(input())
x,y=1,0
while(x<num1):
  y+=1
  x=2**y
if(x==num1):
  print("yes")
else:
  print("no")
