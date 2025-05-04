students = {"철수":85, "영희":42, "민수":73, "지영":38}

def check_score():
  for name, score in students.items():
    if score >= 60:
      print(f"{name}: 합격")

    else:
      print(f"{name}: 불합격")

check_score()
