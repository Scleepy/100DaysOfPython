import random
from art import logo

DIFFICULTY_HARD = 5
DIFFICULTY_EASY = 10

def check_answer(number, guess, difficulty):
    if number > guess:
        print("Too low.")
        return difficulty - 1
    else:
        print("Too high.")
        return difficulty - 1

def start_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        difficulty = DIFFICULTY_EASY
    else:
        difficulty = DIFFICULTY_HARD

    number = random.randint(1, 100)

    game_state = True

    while difficulty != 0 and game_state:

        print(f"You have {difficulty} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        if guess == number: 
            print(f"You got it! The answer was {number}.")
            game_state = False
        else:
            difficulty = check_answer(number, guess, difficulty)
    
    if difficulty == 0:
        print("You've run out of guesses, you lose.")

start_game()

    

