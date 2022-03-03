from art import logo, vs
from game_data import data
from random import randint
from os import system

def dice():
    return randint(0, len(data) - 1)

def is_correct(guess, follower_a, follower_b):
    if follower_a > follower_b:
        return guess == "a"
    else:
        return guess == "b"

def start_game():

    print(logo)
    game_state = True

    score = 0
    index_a = dice()
    index_b = dice()
    follower_b = data[index_b]

    while game_state:
        
        index_a = index_b

        while index_a == index_b:
            index_b = dice()
        
        follower_a = data[index_a]["follower_count"]
        follower_b = data[index_b]["follower_count"]

        print(f"Compare A: {data[index_a]['name']}, a {data[index_a]['description']}, from {data[index_a]['country']}")

        print(vs)
        
        print(f"Compare B: {data[index_b]['name']}, a {data[index_b]['description']}, from {data[index_b]['country']}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        system("cls")
        print(logo)

        if is_correct(guess, follower_a, follower_b):
            score += 1
            print(f"You're right! Current score: {score}.")
        else: 
            game_state = False
            print(f"Sorry, that's wrong. Final score: {score}")

start_game()