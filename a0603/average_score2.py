filename = input("파일 이름을 입력하세요: ")
scores = {}
total = 0
count = 0

try:
  file = open("a0603/" + filename, "r")
  for line in file:
    line = line.strip()
  
    name, score_str = line.split(",")
    score = int(score_str)
    total += score
    count += 1

except ValueError:
  print("잘못된 점수 형식이 있습니다.")
except FileNotFoundError:
  print("파일이 존재하지 않습니다.")

else:
  for name, score in scores:
    print(f"{name}: {score}")
  if count > 0:
    average = total / count
    print(f"전체 평균: {round(average, 2)}")

finally:
  file.close()
  print("파일 처리 종료")
