numbers = [10, 5, 0, 2]
for number in numbers:
  try:
    print(100 / number)  
  except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

my_list = [10, 20, 30]
index = int(input())
try:
  print(my_list[index])
except IndexError:
  print("잘못된 인덱스입니다.")


