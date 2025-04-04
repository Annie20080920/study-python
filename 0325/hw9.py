n = int(input("2 이상의 정수를 입력하세요."))
total = 0
if n >= 2:
  for i in range(1, n+1):
    total = total + i
  print(f"총합은 {total} 입니다.")
