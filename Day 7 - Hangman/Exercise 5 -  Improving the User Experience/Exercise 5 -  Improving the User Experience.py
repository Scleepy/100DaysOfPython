import random

from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

chosen_word = random.choice(word_list)

print(logo)

print(f"Psst, the solution is {chosen_word}")

game_state = True

list = ["_" for i in chosen_word]

position = len(stages) - 1

print(list)

while game_state:

    print(stages[position])

    guess = input("Guess a letter: ").lower()

    if guess in list:
        print(f"You've already guessed {guess}")

    for num, letter in enumerate(chosen_word):
        if letter == guess:
            list[num] = guess
    
    if guess not in chosen_word:
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
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
    