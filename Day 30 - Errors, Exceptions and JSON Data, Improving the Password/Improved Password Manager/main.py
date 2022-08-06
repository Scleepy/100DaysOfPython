from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website_name = website_input.get()
    with open("data.json") as data:
        json_data = json.load(data)
        if website_name in json_data:
            email_name = json_data[website_name]["email"]
            password_name = json_data[website_name]["password"]
            messagebox.askokcancel(title=website_name, message=f"Email: {email_name}\nPassword: {password_name}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():

    website_name = website_input.get()
    email_name = email_username_input.get()
    password_name = password_input.get()

    new_data = {
        website_name: {
            "email": email_name,
            "password": password_name
        }
    }

    if(len(website_name) == 0 or len(password_name) == 0):
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")

    else:

        confirmation = messagebox.askokcancel(title=website_name, message=f"These are the details entered: \nEmail: {email_name}\nPassword: {password_name}\nIs it okay to save?")

        if confirmation:
            try:
                with open("data.json", "r") as data:
                    
                    #Reading contents, use "r" to switch to read only mode
                    json_data = json.load(data)

            except FileNotFoundError:
                with open("data.json", "w") as data:
                    json.dump(new_data, data, indent=4) 

            else:
                #Updating contents with new data
                json_data.update(new_data)

                with open("data.json", "w") as data:
                    
                    #Writing new data, use "w" to switch to write mode
                    json.dump(json_data, data, indent=4) 
            finally:
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
website_input = Entry(width=33)
website_input.grid(column=1, row=1)
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

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()