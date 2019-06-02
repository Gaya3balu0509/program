n1,n2=map(int,input().split())
le=list(map(int,input().split()))
for i in range(0,len(le)):
       if i==n2:
           print(le[i-1])
