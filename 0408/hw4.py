numbers = []
total = 0

while True:
  num = int(input("숫자를 입력하세요:"))
  numbers.append(num)
  total += num

  if total >= 30:
    break

print(f"입력한 숫자들: {numbers}")
print(f"총합: {total}")