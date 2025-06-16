from pathlib import Path

filename = input("파일 이름을 입력하세요: ")
scores = []
try:
  with open(Path(__file__).resolve().parent/filename, "r") as file:
    
    for line in file.readlines():
      line = line.strip()
    
      name, score_str = line.split(",")
      score = int(score_str)
      scores.append(score)
      print(f"{name}: {score}")

except ValueError:
  print("잘못된 점수 형식이 있습니다.")
except FileNotFoundError:
  print("파일이 존재하지 않습니다.")

else:
    average = sum(scores) / len(scores)
    print(f"전체 평균: {round(average, 2)}")

finally:
  print("파일 처리 종료")
