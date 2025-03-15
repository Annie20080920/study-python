students = 0
name = input("이름을 입력하세요.")
name2 = input("이름을 입력하세요.")
name3 = input("이름을 입력하세요.")
score = int(input("점수를 입력하세요."))
score2 = int(input("점수를 입력하세요."))
score3 = int(input("점수를 입력하세요."))

def add_student():
 print("학생의 이름을 입력하세요:", name)
 print(name, "의 점수를 입력하세요:", score)
 print("학생의 이름을 입력하세요:", name2)
 print(name2, "의 점수를 입력하세요:",score2)
 print("학생의 이름을 입력하세요:", name3)
 print(name3, "의 점수를 입력하세요:", score3)

add_student()

def calculate_average():
 print(f"(score + score2 + score3)/3 = {students}")
 print("전체 학생의 평균 점수:", students)
calculate_average()

def print_results():
 if score >= students:
  print(name, ":", score, "-합격")
 else:
  print(name, ":", score, "-불합격")
 if score2 >= students:
  print(name2, ":", score2, "-합격")
 else:
  print(name2, ":", score2, "-불합격")
 if score3 >= students:
  print(name, ":", score3, "-합격")
 else:
  print(name3, ":", score3, "-불합격")

print_results()
 
 