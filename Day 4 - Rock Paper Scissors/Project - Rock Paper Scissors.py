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

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)

hand_images = [rock, paper, scissors]

print(hand_images[choice])

print(f"Computer chose: \n{hand_images[computer_choice]}")

if choice >= 3 or choice < 0:
    print("You typed an invalid number, you lose!")
elif choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and choice == 2:
    print("You lose!")
elif computer_choice > choice:
    print("You lose!")
elif choice > computer_choice:
    print("You win!")
elif choice == computer_choice:
    print("It's a draw")    
