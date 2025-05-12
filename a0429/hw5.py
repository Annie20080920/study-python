class Student:
  def __init__(self, name, age, scores):
    self.name = name
    self.age = age
    self.scores = scores

  def get_average(self):
    average = sum(self.scores) / len(self.scores)
    return average
  
  def is_passed(self):
    return self.get_average() >= 60
    
  def __str__(self):
    average = self.get_average()
    passed = self.is_passed()
    return f"이름: {self.name}, 나이: {self.age}, 평균: {average:.2f}, 합격 여부: {passed}"
  
students = Student("김민지", 16, [80, 90, 78]), Student("이철수", 17, [55, 60, 60]), Student("박영희", 15, [100, 100, 90])
for student in students:
  print(student)