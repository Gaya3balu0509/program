n=int(input())
c=0
for i in range(1,n+1):
    if i**2==n:
        c=1
        break
if c==1:
    print("yes")
else:
    print("no")
