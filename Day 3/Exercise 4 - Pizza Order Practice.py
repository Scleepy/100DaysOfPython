print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M , or L ")

add_pepperoni = input("Do you want pepperoni? Y or N ")

extra_cheese = input("Do you want extra cheese? Y or N ")

pizza_price = {"S": 15, "M": 20, "L": 25}
pepperoni_choice = {"YM": 3, "YL": 3, "YS": 2, "NM": 0, "NL": 0, "NS": 0}
cheese_choice = {"Y": 1, "N": 0}

print(f"Your final bill is: ${pizza_price[size] + pepperoni_choice[add_pepperoni + size] + cheese_choice[extra_cheese]}.")