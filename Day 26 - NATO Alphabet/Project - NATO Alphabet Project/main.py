import pandas

nato_phonetics = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dictionary = {row.letter:row.code for index, row in nato_phonetics.iterrows()}

print(phonetic_dictionary)

word = input("Enter a word: ")

result = [phonetic_dictionary[letter] for letter in word.upper()]

print(result)