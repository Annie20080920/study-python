class Calculator:
  def __init__(self, expression):
    self.expression = expression

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
  
  # def calculator(self):
    