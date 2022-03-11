from turtle import Turtle, Screen
from random import choice

turtle = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(sides):
    angle = 360/sides
    for i in range(sides):
        turtle.forward(100)
        turtle.right(angle)

for sides in range(3, 10):
    turtle.color(choice(colours))
    draw_shape(sides)

screen = Screen()
screen.exitonclick()