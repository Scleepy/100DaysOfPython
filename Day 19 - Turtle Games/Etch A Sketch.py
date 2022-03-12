from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forwards():
    turtle.forward(10)

def move_backwards():
    turtle.backward(10)
    
def turn_left():
    # new_heading = turtlea.heading() + 10
    # turtle.setheading(new_heading)
    turtle.left(10)
    
def turn_right():
    # new_heading = turtlea.heading() - 10
    # turtle.setheading(new_heading)
    turtle.right(10)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()