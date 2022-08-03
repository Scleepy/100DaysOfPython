import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="Label Test", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.place(x=100, y=200)

#Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label["text"] = new_text

button = tkinter.Button(text="Click Me", command=button_clicked)
button.place(x=100, y=100)

#Input Fields
input = tkinter.Entry(width=10)
input.place(x=200, y=100)


window.mainloop()