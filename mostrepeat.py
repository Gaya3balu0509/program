str1=str(input())
max1=0
for i in str1:
    if  str1.count(i)>max1:
        max1=str1.count(i)
        s=i
print(s)
