import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=10, pady=10)

mile_input = tkinter.Entry(width=10)
mile_input.insert(tkinter.END, string="0")
mile_input.grid(column=2, row=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=3, row=1)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=1, row=2)

result_label = tkinter.Label(text="0")
result_label.grid(column=2, row=2)

km_label = tkinter.Label(text="Km")
km_label.grid(column=3, row=2)

mile_to_kilometer = 1.609

def calculate():
    miles = mile_input.get()
    result = float(miles) * mile_to_kilometer
    result_label.config(text=result)


calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.grid(column=2, row=3)


window.mainloop()