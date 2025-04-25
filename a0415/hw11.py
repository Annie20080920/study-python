import random

def play_game():
  answer = generate_answer()
  
  while True:
    guess = get_user_input()
    strikes, balls = count_strikes_and_balls(answer, guess)
    
    if strikes == 3:
      print("3 스트라이크 0 볼")
      print("정답입니다!")
      break

    else:
      print(f"{strikes} 스트라이크 {balls} 볼")

def generate_answer():
  return random.sample(range(1,10), 3)

def get_user_input():
  user_input = input("1부터 9까지의 숫자 3개를 입력하세요. (예: 1 2 3):")
  guess = list(map(int, user_input.split()))

  return guess

def count_strikes_and_balls(answer, guess):
  strikes = 0
  balls = 0
  
  for s, g in zip(answer, guess):
    if s == g:
      strikes += 1
    elif g in answer:
      balls += 1
  return strikes, balls

play_game()


  

  

