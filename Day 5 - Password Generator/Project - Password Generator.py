import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

num_letters = ""
num_symbols = ""
num_numbers = ""

while num_letters == "":
    num_letters = input("How many letters would you like in your password?\n")
while num_symbols == "":
    num_symbols = input(f"How many symbols would you like?\n")
while num_numbers == "":
    num_numbers = input(f"How many numbers would you like?\n")

num_letters = int(num_letters)
num_symbols = int(num_symbols)
num_numbers = int(num_numbers)

char_list = []

for i in range(0, num_letters):
    char_list.append(letters[random.randint(0, len(letters) - 1)])

for i in range(0, num_symbols):
    char_list.append(symbols[random.randint(0, len(symbols) - 1)])

for i in range(0, num_numbers):
    char_list.append(numbers[random.randint(0, len(numbers) - 1)])

random.shuffle(char_list)

password = "".join(char_list)

print(f"Your password is: {password}")