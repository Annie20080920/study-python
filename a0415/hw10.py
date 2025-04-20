import time

def countdown():
  while True:
    start = int(input("몇 초 후에 발사할까요? (0이상 숫자 입력):"))
    if start < 0:
      print("0 이상 숫자만 입력하세요")
    else:
      break

  while start >= 0:
    print(start)
    time.sleep(1)
    start -= 1

  print("🚀 발사!") 

countdown()