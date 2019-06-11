stng1,stng2,num=map(str,input().split())
c=0
for i in range(len(stng1)):
    if stng1[i]!=stng2[i]:
        c=c+1
if c==int(num):
    print("yes")
else:
    print("no")
