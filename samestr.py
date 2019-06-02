lis=list(map(str,input().split()))
a=lis[0]
b=lis[1]
print(a[len(a)-int(b)::])
