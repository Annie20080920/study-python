scores = [90, 25, 67, 45, 80]
number = [1, 2, 3, 4, 5]
for x, y in zip(number, scores):
    if y >= 60:
      print(x,"번 학생은 합격입니다.")
    else:
      print(x,"번 학생은 불합격입니다.")