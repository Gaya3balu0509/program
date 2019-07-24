a=int(input())
l1=list(map(int,input().split()))
for i in range(0,len(l1)-1):
    for j in range(i+1,len(l1)):
        if l1[i]+l1[j]==0:
            print(l1[i],l1[j])
