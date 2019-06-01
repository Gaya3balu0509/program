nu1=int(input())
ct=0
for i in range(1,nu1+1):
    if  nu1%i==0:
        ct+=1
if ct==2:
    print("yes")
else:
    print("no")
