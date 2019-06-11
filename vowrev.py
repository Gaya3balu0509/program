n=int(input())
str=input()
s=""
vowel="AEIOUaeiou"
for i in str:
    if i not in vowel:
         s=s+i
print(s[::-1])
