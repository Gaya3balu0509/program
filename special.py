str1=input()
str2="!@#$%^&*()<>_?.{}"
cnt=0
for i in str1:
    if i in str2:
        cnt=cnt+1
        pass
print(cnt)
