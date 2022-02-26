from art import logo
import os

print(logo)

print("Welcome to the secret auction program.")

bidders = {}

state = True

while state:    
    name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))

    bidders[name] = bid_amount

    ans = input("Are there any other bidders? Type 'yes' or 'no': ")
    if ans == 'no':
        state = False
    os.system("cls")

max_bid = 0
for name in bidders:
    if bidders[name] > max_bid:
        max_bid = bidders[name]
        winner_name = name

print(f"The winner is {winner_name} with a bid of ${max_bid}.")