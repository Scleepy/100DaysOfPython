import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(f"Psst, the solution is {chosen_word}")

guess = input("Guess a letter: ").lower()

list = []

for letter in chosen_word:
    if letter == guess:
        list.append(guess)
    else:
        list.append("_")

print(list)

