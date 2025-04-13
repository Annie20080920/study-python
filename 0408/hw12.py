class Student:
  def __init__(self, name, score):
    self.name = name
    self.score = score
  
  def introduce(self):
    print(f"안녕하세요, 제 이름은 {self.name}이고, 점수는 {self.score}점입니다.")

student1 = Student("영희", 95)
student1.introduce()