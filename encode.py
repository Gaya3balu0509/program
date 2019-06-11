nstr=input()
for i in nstr:
    if ord(i)<88 :
        print(chr(ord(i)+3),end="")
    else:
        print(chr(ord(i)-23),end="")
