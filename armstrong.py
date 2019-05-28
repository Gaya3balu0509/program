num1=int(input())
num=num1
am=0
while(num>0):
  r=num%10
  am=am+(r*r*r)
  num=num//10
if num1==am:
  print("yes")
else:
  print("no")
