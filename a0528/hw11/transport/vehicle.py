class Vehicle:
  def __init__(self, brand):
    self.brand = brand
  
  def describe(self):
    print(f"이 차량은 {self.brand} 브랜드입니다.")