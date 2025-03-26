score = input()
score = list(map(float, score.split()))

average = (score[0] + score[1] + score[2]) / len(score)
average1 = float(average) 
if score[0] >= 40 and score[1] >= 40 and score[2] >= 40:
 if average1 >= 50:
  print("재시험 없음")
else:
  print("재시험 있음")

