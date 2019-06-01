lis=list(input().split())
a=lis[0]
b=lis[1]
if len(a)==len(b):
    print(b)
else:
    if len(a)>len(b):
        print(a)
    else:
        print(b)
