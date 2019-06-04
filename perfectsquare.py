import math
a,b=map(int,input().split())
c=a*b
d=int(math.sqrt(c))
if(d*d==c and d*d==0):
    print("yes")
else:
    print("no")
