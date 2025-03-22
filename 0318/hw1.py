grade = int(input())
if grade >= 90:
  if grade >= 95:
    print("A+")
  else:
    print("A")
elif grade >= 80:
  if grade >= 85:
    print("B+")
  else:
    print("B")
elif grade >= 70:
  if grade >= 75:
    print("C+")
  else:
    print("C")
else:
  print("F")