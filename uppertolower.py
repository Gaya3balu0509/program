stng=input()
for i in stng:
    if i.isupper():
        print(chr(ord(i)+32),end="")
    elif i.islower():
        print(chr(ord(i)-32),end="")
