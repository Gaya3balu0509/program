str1=list(input())
val=len(str1)//2
if len(str1)%2==0:
    str1[val]="*"
    str1[val-1]="*"
else:
    str1[val]="*"
for i in str1:
    print(i,end="")
