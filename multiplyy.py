a=int(input())
l1=list(map(int,input().split()))
c=0
for i in range(0,len(l1)):
    te=1
    for j in range (0,len(l1)):
	    if c!=j:
             te=te*l1[j]
    c+=1
    print(te,end=" ")
