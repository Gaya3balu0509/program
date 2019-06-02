n=int(input())
le=list(map(int,input().split()))
j=1
for  i in range(0,len(le)+1):
        if j==le[i]:
            pass
        else:
            print(i)
            break
        j=j+1
