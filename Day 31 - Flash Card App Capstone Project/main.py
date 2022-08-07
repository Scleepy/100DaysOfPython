from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
card = {}
words_dictionary = {}

try:
    words_progress = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    words_full = pandas.read_csv("./data/french_words.csv")
    words_dictionary = words_full.to_dict(orient="records")
else:
    words_dictionary = words_progress.to_dict(orient="records")


def new_card():
    global card, flip_timer
    window.after_cancel(flip_timer)
    card = random.choice(words_dictionary)
    print(card["French"])

    word_canvas.itemconfig(word_title, text="French", fill="black")
    word_canvas.itemconfig(word_word, text=card["French"], fill="black")
    word_canvas.itemconfig(canvas_background, image=image_front_canvas)
    window.after(3000, func=flip_card)

def flip_card():
    word_canvas.itemconfig(word_title, text="English", fill="white")
    word_canvas.itemconfig(word_word, text=card["English"], fill="white")
    word_canvas.itemconfig(canvas_background, image=image_back_canvas)

def known_card():
    words_dictionary.remove(card)
    print(len(words_dictionary))

    new_data = pandas.DataFrame(words_dictionary)
    new_data.to_csv("./data/words_to_learn.csv", index=False)

    new_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

word_canvas = Canvas(width=800, height=526)
image_front_canvas = PhotoImage(file="./images/card_front.png")
image_back_canvas = PhotoImage(file="./images/card_back.png")
canvas_background = word_canvas.create_image(400, 263, image=image_front_canvas)
word_canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)


word_title = word_canvas.create_text(400, 150, text="Title", font=("Ariel", 40 , "italic"))
word_word = word_canvas.create_text(400, 263, text="Word", font=("Ariel", 60 , "bold"))
word_canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=known_card)
right_button.grid(column=1, row=1)

new_card()

window.mainloop()