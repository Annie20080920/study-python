students_score = []
score = int(input())
score1 = int(input())
score2 = int(input())

def add_score(score):
  global students_score
  students_score.append(float(score))

average = ((students_score[0] + students_score[1] + students_score[2]) / len(students_score))
average1 = int(average) 

if average1 >= 50:
  print("재시험 없음")
else:
  print("재시험 있음")

