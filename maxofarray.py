
nu1,nu2=map(int,input().split())
n=input()
lst=list(map(int,input().split()))
lst2=list(map(int,input().split()))
for i in lst2:
    lst.append(i)
    print(max(lst),end=" ")
