import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="Label Test", font=("Arial", 24, "bold"))
my_label.pack(side="left")

#Method 1
my_label["text"] = "New Text"
#Method 2
my_label.config(text="New Text")

#Button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label["text"] = new_text


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

#Input Fields
input = tkinter.Entry(width=30)
input.pack()
input.get()

#Starting Text
input.insert(tkinter.END, string="Some text to begin with.")

#Textbox
text = tkinter.Text(height=5, width=30)
text.focus()
text.insert(tkinter.END, "Example of a multi-line text entry")
print(text.get("1.0", tkinter.END))
text.pack()

#Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale 

def scale_used(value):
    print(value)

scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbox
def checkbox_used():
    print(checked_state.get())

checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbox_used)
checked_state.get()
checkbutton.pack()

#Radiobutton

def radio_used():
    print(radio_state.get())

radio_state = tkinter.IntVar()

radiobutton1 = tkinter.Radiobutton(text="Option1", value = 1, variable=radio_state, command=radio_used)
radiobutton1.pack()

radiobutton2= tkinter.Radiobutton(text="Option2", value = 2, variable=radio_state, command=radio_used)
radiobutton2.pack()

#Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


# import turtle

# tim = turtle.Turtle()
# tim.write("Hello", font=("Times New Roman", 20, "bold"))

window.mainloop()