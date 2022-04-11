import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states = pd.read_csv("50_states.csv")
states_list = states["state"].to_list()
guessed_list = []

while len(guessed_list) < len(states_list):
    answer = screen.textinput(title=f"{len(guessed_list)}/50 States Correct", prompt="What's another state's name?").title()

    if answer == "Exit":
        missing_list = []
        for state in states_list:
            if state not in guessed_list:
                missing_list.append(state)
        new_data = pd.DataFrame(missing_list)
        new_data.to_csv("missing_states.csv")
        break

    if answer in states_list:
        guessed_list.append(answer)
        newTurtle = turtle.Turtle()
        newTurtle.hideturtle()
        newTurtle.penup()
        state_data = states[states["state"] == answer]
        newTurtle.goto(int(state_data["x"]), int(state_data["y"]))
        newTurtle.write(answer)



