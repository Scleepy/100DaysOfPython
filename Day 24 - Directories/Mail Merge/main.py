with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()
print(name_list)


for name in name_list:
    new_name = name.strip("\n")
    with open("./Input/Letters/starting_letter.txt") as starting_letter:
        letter = starting_letter.read()
        new_letter = letter.replace("[name]", new_name)
        with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", "w") as final_letter:
            final_letter.write(new_letter)
