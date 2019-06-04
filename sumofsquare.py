nu1=int(input())
sum1=0
while(nu1>0):
    n=nu1%10
    sum1=sum1+(n*n)
    nu1=nu1//10
print(sum1)
