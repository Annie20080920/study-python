import time
def countdown():
  start = int(input("몇 초 타이머를 설정할까요?"))

  for i in range(start,0, -1):
    print(i)
    time.sleep(1)

  print("타이머 끝!") 

countdown()