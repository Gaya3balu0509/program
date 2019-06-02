nu1,nu2=map(int,input().split())
z=0
for i in range(nu1,nu2+1):
    ct=0
    for j in range(1,i+1):
        if  i%j==0:
            ct=ct+1
    if ct==2:
        z=z+1
print(z)
