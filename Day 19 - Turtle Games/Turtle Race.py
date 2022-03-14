from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_collection = []

start = -70

for newTurtle in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(newTurtle)
    turtle.penup()
    turtle.goto(x = -230, y = start)
    start += 30
    turtle_collection.append(turtle);
    
game_state = True

while game_state:

    for turtle in turtle_collection:
        random_distance = randint(0, 10)
        turtle.forward(random_distance)

        if turtle.xcor() > 230:
            game_state = False
            win = turtle.pencolor()
            if win == user_bet:
                print(f"You've won! The {win} turtle is the winner!")
            else:
                print(f"You've lost! The {win} turtle is the winner!")


screen.exitonclick()