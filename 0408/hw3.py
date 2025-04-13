numbers = []
for i in range(5):
  num = int(input())
  numbers.append(num)

for num in numbers:
  if num % 2 == 0:
    print(num)