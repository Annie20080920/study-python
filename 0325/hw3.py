def calculator(operation):
  match operation:
    case ("add", a, b):
      print(a + b)
    case ("subtract", a, b):
      print(a - b)
    case ("multiply", a, b):
      print(a * b)
    case ("divide", a, b):
      print( a / b)
    case ("divide", a, b):
      print("0으로 나눌 수 없습니다.")
    case _:
      print("잘못된 입력")

calculator(["divide", 10, 2])
