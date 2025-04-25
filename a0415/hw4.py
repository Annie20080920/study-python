import time

input("시작하려면 Enter 키를 눌러주세요.")
start = time.time()

input("입력을 완료하려면 Enter 키를 눌러주세요.")
end = time.time()

print(f"입력 시간: {end - start: .2f} 초")

