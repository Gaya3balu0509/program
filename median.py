num1=int(input())
lst=list(map(int,input().split()))
lst.sort()
n=len(lst)//2
print(lst[n])
