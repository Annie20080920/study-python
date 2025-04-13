class Car:
  def __init__(self, maker, year):
    self.maker = maker
    self.year = year
  
  def info(self):
    print(f"이 차의 제조사는 {self.maker}이고, {self.year}년 식 입니다")

car = Car("Audi", 2025)
car.info()