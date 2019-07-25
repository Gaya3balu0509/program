a=int(input())
l3=[]
l=list(map(int,input().split()))
flag=0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            l3.append(j)
m=min(l3)
print(l[m])
