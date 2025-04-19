total = 0

while True:
  num = input()
  if num.isdigit():
    num1 = int(num)
    total += num1
  
  else:
    print("숫자를 입력하세요")

  if num1 == 0:
    break

print("총합:", total)