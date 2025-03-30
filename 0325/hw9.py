n = int(input("2 이상의 정수를 입력하세요."))
if n >= 2:
  total = sum(range(1, n+1))
  print(f"총합은 {total} 입니다.")
