a=int(input())
l1=list(map(int,input().split()))
l3=[]
for i in l1:
    if l1.count(i)>1:
        if i not in l3:
            l3.append(i)
l3.sort()
print(*l3,end=' ')
