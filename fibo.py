num1=int(input())
a,b=0,1
print(b,end=" ")
for i in range(1,num1):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
