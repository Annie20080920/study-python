class Calculator:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2

  def add(self):
    print("더하기:", self.num1 + self.num2)

  def subtract(self):
    print("빼기:", self.num1 - self.num2)

  def multiply(self):
    print("곱하기:", self.num1 * self.num2)

  def divide(self):
    print("나누기:", self.num1 / self.num2)

cal = Calculator(5, 2)
cal.add()
cal.subtract()
cal.multiply()
cal.divide()