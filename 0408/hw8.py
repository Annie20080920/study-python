number = (input())

number1 = map(int, number.split(" "))

max = 0
for i in number1:
  if i > max:
    max = i

print(max)
  
# max_num = max(number1)
# print(max_num)
