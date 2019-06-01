num1=str(input())
for i in range(0,len(num1)):
    if num1[i]!='0' and num1[i]!='1':
        print("no")
        break
else:
    print("yes")
