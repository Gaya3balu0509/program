a=int(input())
lis=list(map(int,input().split()))
av=0
for i in range(0,len(lis)):
    av=av+lis[i]
print(av//a)
