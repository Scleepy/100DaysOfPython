from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate():
    password_input.delete(0, END)
    password_letters = [random.choice(letters) for i in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for i in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for i in range(random.randint(2, 4))]

    char_list = password_letters + password_symbols + password_numbers
    random.shuffle(char_list)
    password = "".join(char_list)

    password_input.insert(0, password)
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():

    website_name = website_input.get()
    email_name = email_username_input.get()
    password_name = password_input.get()

    if(len(website_name) == 0 or len(password_name) == 0):
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")

    else:

        confirmation = messagebox.askokcancel(title=website_name, message=f"These are the details entered: \nEmail: {email_name}\nPassword: {password_name}\nIs it okay to save?")

        if confirmation:
            with open("data.txt", "a") as data:
                data_format = f"{website_name} | {email_name} | {password_name}\n"
                data.write(data_format)

                website_input.delete(0, END)
                password_input.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

image_canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
image_canvas.create_image(100, 100, image=logo_image)
image_canvas.grid(column=1, row = 0)

#LABELS
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#INPUTS
website_input = Entry(width=52)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_username_input = Entry(width=52)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(END, "daniel@gmail.com")

password_input = Entry(width=33)
password_input.grid(column=1, row=3)

#BUTTONS
generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()