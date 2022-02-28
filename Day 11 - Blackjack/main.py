from art import logo
import os
import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_game():
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        os.system("cls")
        black_jack()
    else:
        os.system("cls")

def calc(list):

    if sum(list) == 21 and len(list) == 2:
        return 0

    if 11 in list and sum(list) > 21:
        list.remove(11)
        list.append(1)
    return sum(list)

def winner(user_score, comp_score):
    if user_score > 21 and comp_score > 21:
        return "You went over. You lose 😤"
    elif user_score == comp_score:
        return "Draw 🙃"
    elif comp_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif comp_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > comp_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def black_jack():
    print(logo)

    user_cards = []
    comp_cards = []
    user_score = 0
    comp_score = 0
    game_state = True

    for i in range (0, 2):
        user_cards.append(random.choice(deck))
        comp_cards.append(random.choice(deck))

    
    while game_state:
        user_score = calc(user_cards)
        comp_score = calc(comp_cards)

        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_state = False
        
        deal_again = input("Type 'y' to get another card, type 'n' to pass: ")
        
        if deal_again == "y":
            user_cards.append(random.choice(deck))
        else:
            game_state = False

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(random.choice(deck))
        comp_score = calc(comp_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {comp_cards}, final score: {comp_score}")

    print(winner(user_score, comp_score))
    play_game()

play_game()