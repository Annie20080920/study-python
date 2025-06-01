class Vehicle:
  def __init__(self, brand):
    self.brand = brand

class Car(Vehicle):
  def __init__(self, brand, model):
    super().__init__(brand)
    self.model = model

  def info(self):
    print(f"{self.brand} - {self.model}")

c = Car("현대", "아반떼")
c.info()
    