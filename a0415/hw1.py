import random

def number_guessing_game():
  answer = random.randint(1,100)
  attempts = 0

  while True:
    guess = int(input("입력 값:"))
    attempts += 1

    if guess < answer:
      print("컴퓨터: 더 높게! ")
    elif guess > answer:
      print("컴퓨터: 더 낮게!")
    else:
      print("컴퓨터: 정답!")
      print(f"시도 횟수: {attempts}")
      break

number_guessing_game()