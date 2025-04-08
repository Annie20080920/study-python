choices = ["가위", "바위", "보"]
user = input("가위, 바위, 보 중 하나를 입력하세요:")

computer = choices[0]

print(f"가위, 바위, 보 중 하나를 입력하세요: {user}")
print(f"사용자: {user}, 컴퓨터: {computer}")

if user == computer:
  print("비겼습니다!")
elif user == "보" and computer == "가위":
  print("컴퓨터가 이겼습니다.")
elif user == "바위" and computer == "가위":
  print("사용자가 이겼습니다.")
elif user not in choices:
  print("잘못된 입력입니다!")

choices.append(choices.pop(0))