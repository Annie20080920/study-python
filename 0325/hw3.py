def calculator(operation):
  match operation:
    case ("add", a, b):
     return(a + b)
    case ("subtract", a, b):
      return(a - b)
    case ("multiply", a, b):
      return(a * b)
    case ("divide", a, b):
      return( a / b)
    case ("divide", a, 0):
      return("0으로 나눌 수 없습니다.")
    case _:
      return("잘못된 입력")

print(calculator(("divide", 10, 0)))
