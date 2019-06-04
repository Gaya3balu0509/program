num1,num2=map(int,input().split())
lst=list(map(int,input().split()))
k=0
for i in lst:
    if i%2!=0:
        odd=i
        k=k+1
        if k==num2:
            print(i)
            break
