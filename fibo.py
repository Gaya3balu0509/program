num1=int(input())
a,b=0,1
print(b,end=" ")
for i in range(1,num1):
    ne=a+b
    print(ne,end=" ")
    a=b
    b=ne
