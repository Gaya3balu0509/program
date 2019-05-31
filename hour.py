time=int(input())
hr=0
if time<60:
    print(hr,time)
else:
    hr=time//60
    time=time%60
    print(hr,end=" ")
    print(time)
