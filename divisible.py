num1,num2=map(int,input().split())
for i in range(1,(num1*num2)+1):
    if i%num1==0 and i%num2==0:
        print(i)
        break
