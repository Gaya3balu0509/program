l=list(map(int,input().split()))
a=l[0]
b=l[1]
m=l[2::]
s=0
for i in range(0,b):
    s=s+m[i]
print(s)
