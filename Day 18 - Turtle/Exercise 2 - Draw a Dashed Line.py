from turtle import Turtle, Screen

turtle = Turtle()

for i in range (0, 6):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

screen = Screen()
screen.exitonclick()