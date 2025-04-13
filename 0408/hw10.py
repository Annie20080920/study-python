number = float(input())
number1 = round(number)
number2 = range(1,10)

for x in number2:
  print(f"{number1} * {x} =", number1 * x)