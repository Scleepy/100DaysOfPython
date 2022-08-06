import pandas

nato_phonetics = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dictionary = {row.letter:row.code for index, row in nato_phonetics.iterrows()}

print(phonetic_dictionary)

def generate_phonetic():
    word = input("Enter a word: ")

    try:
        result = [phonetic_dictionary[letter] for letter in word.upper()]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()