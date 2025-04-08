choices = ["가위", "바위", "보"]

user_win = 0
computer_win = 0
no_win = 0

for i in range(5):
  user = input("가위, 바위, 보 중 하나를 입력하세요:")
  computer = choices[0]
  print(f"게임 {i+1}: 가위, 바위, 보 중 하나를 입력하세요: ")
  print(f"사용자: {user}, 컴퓨터: {computer}")

  if user not in choices:
    print("잘못된 입력입니다!")
  elif user == computer:
    print("비겼습니다!")
    no_win = no_win+1
  elif (user == "가위" and computer == "보") or (user == "바위" and computer == "가위") or (user == "보" and computer == "바위"):
    print("사용자가 이겼습니다!")
    user_win = user_win+1
  else:
    print("컴퓨터가 이겼습니다!")
    computer_win = computer_win+1
  
  choices.append(choices.pop(0))

total_games = 5
user_rate = (user_win / total_games) * 100
computer_rate = (computer_win / total_games) * 100
draw_rate = (no_win / total_games) * 100

print("--- 최종 결과 ---")
print(f"사용자 승률: {user_rate}%")
print(f"컴퓨터 승률: {computer_rate}%")
print(f"비긴 게임 비율: {draw_rate}%")

if user_rate > computer_rate:
    print("사용자가 최종 승리했습니다!")
elif user_rate < computer_rate:
    print("컴퓨터가 최종 승리했습니다!")
else:
    print("동점입니다.")



