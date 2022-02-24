import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(f"Psst, the solution is {chosen_word}")

game_state = True

list = ["_" for i in chosen_word]

position = len(stages) - 1

print(list)

while game_state:

    print(stages[position])

    guess = input("Guess a letter: ").lower()

    for num, letter in enumerate(chosen_word):
        if letter == guess:
            list[num] = guess
    
    if guess not in chosen_word:
      position -= 1

    print(list)

    if '_' not in list:
        game_state = False
        print("You win!")
        print(f"Word is {chosen_word}.")
    elif position == 0:
        print(stages[position])
        game_state = False
        print("You lose!")
        print(f"Word is {chosen_word}.")
    