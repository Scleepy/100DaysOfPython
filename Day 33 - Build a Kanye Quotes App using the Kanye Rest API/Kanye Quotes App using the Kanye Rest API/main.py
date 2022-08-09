from tkinter import *
import requests

def get_quote():
    url = "https://api.kanye.rest/"

    response_data = requests.get(url).json()
    quote = response_data["quote"]
    canvas.itemconfig(quote_text, text=quote)

    print(quote)



#UI

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_image = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_image)
quote_text = canvas.create_text(150, 207, text="Placeholder", width=250, font=("Arial", 25, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_image = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_image, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()