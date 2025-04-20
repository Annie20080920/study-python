import time

start = time.time()
print("시작하려면 Enter 키를 눌러주세요.")

for i in range(1000000):
  pass
end = time.time()
print("입력을 완료하려면 Enter 키를 눌러주세요.")

print("입력 시간:", end - start, "초")

