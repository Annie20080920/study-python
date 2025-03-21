students = []
student_score = []

def add_student(name, score):
 global students, student_score
 students.append(name)
 student_score.append(float(score))

def calculate_average():
 average = (student_score[0] + student_score[1] + student_score[2]) / len(student_score)
 return average

def print_results(average):
 if score >= average:
  print(name, ":", score, "-합격")
 else:
  print(name, ":", score, "-불합격")

 if score2 >= average:
  print(name2, ":", score2, "-합격")
 else:
  print(name2, ":", score2, "-불합격")

 if score3 >= average:
  print(name, ":", score3, "-합격")
 else:
  print(name3, ":", score3, "-불합격")

name = input("이름을 입력하세요.")
score = int(input(f"{name}의 점수를 입력하세요."))
add_student(name, score)
name2 = input("이름을 입력하세요.")
score2 = int(input(f"{name2}의 점수를 입력하세요."))
add_student(name2, score2)
name3 = input("이름을 입력하세요.")
score3 = int(input(f"{name3}의 점수를 입력하세요."))
add_student(name3, score3)

average = calculate_average()
print("전체 학생의 평균 점수:", average)

print_results(average)
 
 