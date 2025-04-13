class Animal:
  def __init__(self,name):
    self.name = name
  
  def introduce(self):
    print(f"저는 {self.name} 입니다.")

animal = Animal("바둑이")
animal.introduce()
    