n=int(input())
n1,n2=map(int,input().split())
for i in range(n1+1,n2):
    if i==n:
        print("yes")
        break
else:
    print("no")
