numb1=str(input())
for i in range(0,len(numb1)):
    if numb1[i]!='0' and numb1[i]!='1':
        print("no")
        break
else:
    print("yes")
