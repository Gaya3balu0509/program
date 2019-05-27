n1=int(input())
a=n1
s=0
while(a>0):
  r=a%10
  s=(s*10)+r
  a=a//10
if s==n1:
  print("yes")
else:
  print("no")
