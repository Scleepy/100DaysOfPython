import turtle
import time
from snake import Snake

screen = turtle.Screen()

screen.setup(width = 600, height = 800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_state = True

while game_state:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()