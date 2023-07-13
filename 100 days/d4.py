# To create a rock-paper-scissors game

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


user_input = int(input("What do you want to choose : \n1.Rock\n2.Paper\n3.Scissors\n:::::"))
game_images = [rock, paper, scissors]
if user_input >= 4 or user_input < 1:
  print("Choose a valid response and try again.")
else:
  print(game_images[user_input-1])
  comp_input = random.randint(1, 3)
  print("\nComputer chose : ", comp_input)
  print(game_images[comp_input-1])

if user_input >= 4 or user_input < 1:
  print("Try again.")
elif (user_input == comp_input):
  print("Draw")
elif user_input == 1 and comp_input == 3:
  print("you win")
elif user_input == 3 and comp_input == 1:
  print("You lose")
elif user_input > comp_input:
  print("You win")
else:
  print("you lose")
