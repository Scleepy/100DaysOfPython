import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

turtle.speed("fastest")
turtle.color(random_color())
turtle.circle(100)

def draw(gap):
    for i in range(int(360/gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + gap)

draw(5)

screen = t.Screen()
screen.exitonclick()