total = 0

while True:
  num = int(input())
  total += num

  # if type(num) != int:
  #   print("숫자를 입력하세요")

  if num == 0:
    break

print("총합:", total)