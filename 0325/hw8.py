scores = [90, 25, 67, 45, 80]
for x,y in enumerate(scores, start=1):
  if y >= 60:
      print(x,"번 학생은 합격입니다.")
  else:
      print(x,"번 학생은 불합격입니다.")
