import math
a,b=input().split()
c=int(a)*int(b)
d=int(math.sqrt(c))
if(d*d==c and d*d!=0):
    print("yes")
else:
    print("no")
