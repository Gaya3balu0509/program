st1=input()
st2="aeiouAEIOU"
c=0
for i in st1:
    if i in st2:
        c=1
        break
if c==1:
    print("yes")
else:
    print("no")
