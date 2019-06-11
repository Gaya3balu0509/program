a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
if a==c==e or b==d==f or (a==b and c==d and e==f):
    print("yes")
else:
    print("no")
