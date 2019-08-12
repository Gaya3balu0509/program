a=int(input())
l1=list(map(int,input().split()))
for i in l1:
    te=1
    for j in l1:
	    if i!=j:
		    te=te*j
    print(te,end=" ")
