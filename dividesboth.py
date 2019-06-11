nu1,nu2=map(int,input().split())
max=1
for i in range(1,nu2):  
    if nu1%i==0 and nu2%i==0:
               max=i
print(max)
