from .vehicle import Vehicle
class Car(Vehicle):
  def __init__(self, brand, model):
    super().__init__(brand)
    self.model = model
  
  def describe(self):
    print(f"이 차량은 {self.brand}의 {self.model} 모델입니다.")

  def drive(self):
    print("출발합니다!")