age = int(input())
height = float(input("cm"))
if age >= 12:
  if height >= 140:
    print("탑승가능")
  elif height <= 140:
   print("키가 부족하여 탑승불가")
else: 
  print("나이가 어려 탑승 불가")