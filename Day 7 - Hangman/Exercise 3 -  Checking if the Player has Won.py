import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(f"Psst, the solution is {chosen_word}")

game_state = True

list = ["_" for i in chosen_word]

print(list)

while game_state:

    guess = input("Guess a letter: ").lower()

    for num, letter in enumerate(chosen_word):
        if letter == guess:
            list[num] = guess

    print(list)

    if '_' not in list:
        game_state = False
        print("You win!")
        print(f"Word is {chosen_word}.")
    

