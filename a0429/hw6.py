class Student:
  def __init__(self, name, score):
    self.name = name
    self.score = score

  def get_grade(self):
    if self.score >= 90:
      return "A"
    elif self.score >= 80:
      return "B"
    elif self.score >= 70:
      return "C"
    else:
      return "F"
    
class School:
  def __init__(self):
    self.students = []

  def add_student(self, student):
    self.students.append(student)

  def print_all(self):
    for student in self.students:
      grade = student.get_grade()
      print(f"이름: {student.name}, 점수: {student.score}, 등급: {grade}")

school = School()
school.add_student(Student("김민지", 87))
school.add_student(Student("이철수", 93))
school.add_student(Student("박영희", 72))
school.print_all()