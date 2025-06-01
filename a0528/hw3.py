class Person:
  def __init__(self, name):
    self.name = name
  
  def speak(self):
    print(f"안녕하세요, 제 이름은 {self.name}입니다.")

class Student(Person):
  def __init__(self, name, school):
    super().__init__(name)
    self.school = school

  def speak(self):
    super().speak()
    print(f"저는 {self.school} 학생입니다.")

s = Student("민수", "중앙고")
s.speak()
