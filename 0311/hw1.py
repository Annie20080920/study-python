x = 5
def my_function():
  x = 10
  print(f"함수내부x: {x}")

my_function()
print(f"함수외부x: {x}")

# 실행 결과:
함수내부x: 10
함수외부x: 5