num=int(input())
if num%4==0:
  if num%100==0:
    if num%400==0:
      print("yes")
    else:
      print("no")
  else:
    print("yes")
else:
  print("no")
