
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encrypt(text, shift):
    new_text = ""

    for letter in text:
        new_letter = alphabet[alphabet.index(letter) + shift]
        new_text += new_letter

    return new_text

def decrypt(text, shift):
    new_text = ""

    for letter in text:
        new_letter = alphabet[alphabet.index(letter) - shift]
        new_text += new_letter

    return new_text

state = True

from art import logo

print(logo)

while state:
    method = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    if method == "encode":
        new_word = encrypt(text, shift)
    else:
        new_word = decrypt(text, shift)

    print(f"Here's the {method}d result: {new_word}")

    again = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    
    if again == "no":
        state = False
        print("Goodbye")
        
