# new features
# elif command == play
import random
dead = False
while not dead:
  computer = random.choice(["rock", "scissors", "paper"])
  user = input("choose one of rock, scissors, paper:")

  print(f"You: {user}, Enemy: {computer}")

  if user == computer:
    print("You've got the same one with him. Do you want to play again?")
    command = input(">")
    if command == "Yes":
      dead = False
    else:
      dead = True
    
  elif user == "rock":
    if computer == "scissors":
      print("Congratulations! You've won the mini game!!")
    elif computer == "paper":
      print("Ooops, you lost the game.")
      print("That's the end of the game.")

    dead = True
  elif user == "paper":
    if computer == "scissors":
      print("Ooops, you lost the game.")
      print("That's the end of the game.")
    elif computer == "rock":
      print("Congratulations! You've won the mini game!!")

    dead = True
  elif user == "scissors":
    if computer == "rock":
      print("Ooops, you lost the game.")
      print("That's the end of the game.")
    elif computer == "paper":
      print("Congratulations! You've won the mini game!!")

    dead = True
  else:
      print("Select again, please")
      dead = False

