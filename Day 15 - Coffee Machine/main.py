from os import system

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

machine_state = True

def check_ingredients(drink_ingredients):
    for ingredients in drink_ingredients:
        if drink_ingredients[ingredients] > resources[ingredients]:
            print(f"Sorry there is not enough {ingredients}")
            return False
    return True

def get_input():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

while machine_state:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    
    if choice == "off":
        machine_state = False
        system("cls")
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[choice]

        if check_ingredients(drink["ingredients"]):
            total = get_input()

            if total >= drink["cost"]:
                change = round(total - drink["cost"], 2)

                print(f"Here is ${change} in change.")

                money += drink["cost"]

                for ingredients in drink["ingredients"]:
                    resources[ingredients] -= drink["ingredients"][ingredients]

                print(f"Here is your {choice} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")