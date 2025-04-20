import random

class Dice:
  def roll(self):
    return random.randint(1,6)
  
  def play_game():
    player_score = 0
    computer_score = 0
    round = 1
    dice = Dice()
    
    while player_score < 2 and computer_score < 2:
      print(f"Round {round}")
      player_roll = dice.roll()
      computer_roll = dice.roll()

      print(f"나: {player_roll}, 컴퓨터: {computer_roll}", end=" → ")

      if player_roll > computer_roll:
        player_score += 1
        print("나 승!")

      elif player_roll < computer_roll:
        computer_score += 1
        print("컴퓨터 승!")

      else:
        print("비겼습니다!")

      round += 1
      print()

    if player_score == 2:
      print("내가 이겼습니다!")

    else:
      print("컴퓨터가 이겼습니다.")

Dice.play_game()

