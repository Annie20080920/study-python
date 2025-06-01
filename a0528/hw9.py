class Employee:
  def greet(self):
    print("안녕하세요. 저는 직원입니다.")

class Manager(Employee):
  def __init__(self, name):
    self.name = name

  def greet(self):
    super().greet()
    print(f"제 이름은 {self.name}이고, 저는 매니저입니다.")

m = Manager("Lee")
m.greet()
