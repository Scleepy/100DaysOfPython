import turtle
from newTurtle import NewTurtle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

left_turtle = NewTurtle((350, 0))
right_turtle = NewTurtle((-350, 0))

screen.listen()
#Player on the left
screen.onkey(left_turtle.go_up, "Up")
screen.onkey(left_turtle.go_down, "Down")
#Player on the right
screen.onkey(right_turtle.go_up, "w")
screen.onkey(right_turtle.go_down, "s")

game_state = True

ball = Ball()
scoreboard = Scoreboard()

while game_state:
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_turtle) < 50 and ball.xcor() > 320 or ball.distance(right_turtle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()