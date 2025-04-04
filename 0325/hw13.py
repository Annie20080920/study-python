number = range(2,10)
number2 = range(1,10)
for x in number:
  for y in number2:
    print(f"{x} * {y} =", x * y)
  print("-------------------")