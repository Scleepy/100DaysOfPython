from turtle import Turtle, Screen
from random import choice

turtle = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
turtle.pensize(15)
turtle.speed("fastest")

for i in range(200):
    turtle.color(choice(colours))
    turtle.forward(30)
    turtle.setheading(choice(directions))

screen = Screen()
screen.exitonclick()