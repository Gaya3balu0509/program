lst=list(map(int,input().split()))
for x in range(lst[0]+1,lst[1]):
  if x%2!=0:
    print(x,end=" ")
