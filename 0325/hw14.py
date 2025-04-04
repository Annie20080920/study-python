name = input("학생ㅣ름:").split(",")
score = list(map(int(input("학생 점수").split(","))))

def print_results():
 average = sum(score) / len(score)
 
 for name, score in zip(name, score):
  if score >= average:
   result = "합격"
  else:
   result = "불합격"
 
 print(f"{name}: {score}점 -> {result}")

print_results()