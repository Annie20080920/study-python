def countdown():
  while True:
    start = int(input("몇 초 타이머를 설정할까요?"))
    if start < 0:
      print("0 이상 숫자만 입력하세요")
    else:
      break

  while start > 0:
    print(start)
    start -= 1

  print("타이머 끝!") 

countdown()