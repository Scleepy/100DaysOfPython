import random

names_string = input("")

names = names_string.split(",")

print(f"{names[random.randint(0,len(names)-1)]} is going to buy the meal today!")
