l=list(map(int,input().split()))
a=l[0]
b=l[1]
for i in range (a+1,b):
   c=0 
   for j  in range(1,i+1):
     if i%j==0:
       c=c+1
   if c==2:
       print(i,end=" ")
