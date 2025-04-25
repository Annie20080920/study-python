import random

class Dice:
  def play_game(self):
    player_score = 0
    computer_score = 0
    round = 1
    
    while player_score < 2 and computer_score < 2:
      print(f"Round {round}")
      player_roll = self.roll()
      computer_roll = self.roll()

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
  

    if player_score == 2:
      print("내가 이겼습니다!")

    else:
      print("컴퓨터가 이겼습니다.")
  
  def roll(self):
    return random.randint(1,6)

dice = Dice()
dice.play_game()

