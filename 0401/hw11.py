def factorial(n):
  if n > 0:
    total = 1
    for i in range(1,n+1):
      total = total * i
    return total
  else:
    return "잘못 입력하였습니다."


n = int(input())
print(factorial(n))