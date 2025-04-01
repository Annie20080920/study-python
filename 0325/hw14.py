name = input("이름을 입력하세요.").split(",")
score = int(input(f"{name}의 점수를 입력하세요.")).split(",")

average = (score[0] + score[1] + score[2]) / len(score)
 
def print_results(average, name, score):
 for i in zip(name, score):
  if score >= average:
   result = "합격"
  else:
   result = "불합격"
   print(f"{name}: {score}점 -> {result}")

print_results(average, name, score)