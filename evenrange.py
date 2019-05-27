m=list(map(int,input().split())
a=m[0]
b=m[1]
for i in range(a+1,b):
  if i%2==0:
    print(i,end=" ")
