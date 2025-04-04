n = int(input("0보다 큰 정수를 입력하세요."))
if n > 0:
  for i in range(1, n+1):
    print( " " * (n - i) + "*" * (2*i - 1))
    