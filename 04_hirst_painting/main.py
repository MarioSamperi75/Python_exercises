import colorgram
import random
import turtle
from turtle import Turtle, Screen

# Extract 20 colors from an image.
colors = colorgram.extract('image.JPG', 100)
colors_list = []

for color in colors:
    colors_list.append((color.rgb.r, color.rgb.g, color.rgb.b))


turtle.colormode(255)
tim = Turtle()
tim.shape("triangle")
tim.penup()
tim.speed(0)

# colors_list = [(14, 26, 36), (111, 94, 71), (75, 100, 122), (37, 27, 15), (182, 159, 120), (12, 20, 18), (86, 101, 96), (157, 135, 85), (41, 28, 36), (137, 151, 165), (235, 218, 172), (104, 125, 162), (235, 199, 126), (151, 165, 161), (99, 83, 89), (91, 68, 24), (147, 137, 145), (39, 72, 83), (80, 53, 64), (42, 64, 89)]

def set_start_position():
    tim.setx(-280)
    tim.sety(-200)


def pick_random_color():
    rand_color = random.choice(colors_list)
    return rand_color


def draw_dot_line():
    for _ in range(10):
        tim.forward(50)
        tim.dot(20, pick_random_color())


def move_line_up():
    tim.setx(-280)
    tim.left(90)
    tim.forward(50)
    tim.right(90)


set_start_position()

for _ in range(10):
    draw_dot_line()
    move_line_up()

tim.hideturtle()


screen = Screen()
screen.exitonclick()

