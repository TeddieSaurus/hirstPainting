import random
import turtle

import colorgram

rgb_colors = []
colors = colorgram.extract("image.jpg",6)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append((new_color))
print(rgb_colors)
color_list = ['#ffa9ff','#65ff7f','#fffa65','#ff6f59','#4bffed']

painter = turtle.Turtle()
painter.speed(0)
painter.hideturtle()


def draw_10_dots():
    for _ in range(10):
        painter.dot(20,random.choice(color_list))
        painter.penup()
        painter.forward(30)
        painter.pendown()


def move_up():
    painter.penup()
    painter.setheading(90)
    painter.forward(30)
    painter.setheading(180)
    painter.forward(300)
    painter.setheading(0)


def draw_hirst():
    for _ in range(10):
        draw_10_dots()
        move_up()


draw_hirst()

my_screen = turtle.Screen()
my_screen.exitonclick()