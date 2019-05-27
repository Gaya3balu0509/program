num=int(input())
if num%4:
  if num%100:
    if num%400:
      print("yes")
    else:
      print("no")
  else:
    print("yes")
else:
  print("no")
