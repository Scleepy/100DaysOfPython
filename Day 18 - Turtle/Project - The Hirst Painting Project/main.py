# import colorgram

# colors = colorgram.extract('img.jpg', 30)

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors) 

import turtle as t 
from random import choice

color_list = [(202, 166, 107), (141, 71, 53), (56, 90, 117), (223, 201, 136), (163, 150, 51), (122, 34, 29), (136, 163, 178), (50, 116, 87), (201, 92, 68), (58, 46, 44), (17, 98, 77), (236, 178, 167), (151, 143, 148), (155, 180, 147), (189, 206, 177), (174, 12, 15), (186, 91, 94), (101, 141, 127), (26, 69, 65), (236, 151, 153)]

turtle = t.Turtle()
t.colormode(255)

turtle.speed("fastest")
turtle.hideturtle()
turtle.setheading(225)
turtle.penup()
turtle.forward(300)
turtle.setheading(0)

num_of_dots = 100

for i in range(1, num_of_dots + 1):
    turtle.dot(20, choice(color_list))
    turtle.penup()
    turtle.forward(50)

    if i % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)



screen = t.Screen()
screen.exitonclick()