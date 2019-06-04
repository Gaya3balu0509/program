numb1=int(input())
a,b=0,1
print(b,end=" ")
for i in range(1,numb1):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
