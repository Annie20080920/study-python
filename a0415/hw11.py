import random

def get_user_input():
  while True:
    user_input = input("숫자 3개를 입력하세요 (예: 1 2 3):")
    guess = list(map(int, user_input.split()))

def count_strikes_and_balls(secret, guess):
  strikes = 0
  balls = 0
  for s, g in zip(secret, guess):
    if s == g:
      strikes += 1
    elif g in secret:
      balls += 1

  return strikes, balls

def play_game():
  secret = random.sample(range(1,10), 3)

  while True:
    guess = get_user_input()
    strikes, balls = count_strikes_and_balls(secret, guess)