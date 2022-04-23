from random import randint

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
imgs_ = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_choice == 0:
    print(imgs_[user_choice])
elif user_choice == 1:
    print(imgs_[user_choice])
elif user_choice == 2:
    print(imgs_[user_choice])

computer_choice = randint(0,2)
if computer_choice == 0:
    print('Computer chose:\n', imgs_[computer_choice])
elif computer_choice == 1:
    print('Computer chose:\n', imgs_[computer_choice])
elif computer_choice == 2:
    print('Computer chose:\n', imgs_[computer_choice])

if (user_choice == 0 and computer_choice == 0) or (user_choice == 1 and computer_choice == 1) or (user_choice == 2 and computer_choice == 2):
    print("Draw.")
elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
    print("You lose.")
else:
    print("You win.")