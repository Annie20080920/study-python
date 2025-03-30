students = []
student_score = []

for i in range(3):
 name = input("이름을 입력하세요.")
 score = int(input(f"{name}의 점수를 입력하세요."))
 students.append(name)
 student_score.append(float(score))

 average = (student_score[0] + student_score[1] + student_score[2]) / len(student_score)
 
def print_results(average, students):
 for name, score in students:
  if score >= average:
   result = "합격"
  else:
   result = "불합격"
   print(f"{name}: {score}점 -> {result}")

print_results(average, students)