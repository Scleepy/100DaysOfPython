from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
HOUR = 60
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():

    global reps
    reps += 1

    work_seconds = WORK_MIN * HOUR
    short_break_seconds = SHORT_BREAK_MIN * HOUR
    long_break_seconds = LONG_BREAK_MIN * HOUR

    if reps % 8 == 0:
        count_down(long_break_seconds)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        timer_label.config(text="Break", fg=PINK)
    else: 
        count_down(work_seconds)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(counter):

    counter_minutes = math.floor(counter / HOUR)
    counter_seconds = counter % 60

    if counter_seconds < 10:
        counter_seconds = f"0{counter_seconds}"

    print(counter)
    canvas.itemconfig(timer_text, text=f"{counter_minutes}:{counter_seconds}")
    if counter > 0:
        global timer
        timer = window.after(1000, count_down, counter-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✓"
        checkmark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

checkmark_label = Label(text="", fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

window.mainloop()
