l=list(map(int,input().split()))
a=l[0]
b=l[1]
for num in range(a,b):
    am=0
    num1=num
    while(num>0):
      r=num%10
      am=am+(r*r*r)
      num=num//10
    if num1==am:
      print(num1)
