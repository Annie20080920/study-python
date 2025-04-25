class Calculator:
  def __init__(self, expression):
    self.expression = expression
  
  def calculate(self):
    part = self.expression.split()

    if len(part) != 3:
      return "입력 형식이 올바르지 않습니다. 예: 10 + 3"
    
    num1, symbol, num2 = part
    num1 = float(num1)
    num2 = float(num2)

    match symbol:
      case "+":
        return f"결과: {self.add(num1, num2)}"
      case "-":
        return f"결과: {self.subtract(num1, num2)}"
      case "*":
        return f"결과: {self.multiply(num1, num2)}"
      case "/":
        return f"결과: {self.divide(num1, num2)}"
      case _:
        return "지원하지 않는 연산자입니다."
  
  def add(self, a, b):
    return a + b
  
  def subtract(self, a, b):
    return a - b
  
  def multiply(self, a, b):
    return a * b
  
  def divide(self, a, b):
    if b == 0:
      return "0으로 나눌 수 없습니다."
    return a / b   
expression = input("계산식을 입력하세요 (예: 10 + 3): ")
calc = Calculator(expression)
print(calc.calculate())
