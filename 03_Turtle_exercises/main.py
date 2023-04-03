import turtle
from turtle import Turtle, Screen
import random

# turtle.colormode(255)
tim = Turtle()
tim.shape("triangle")
# tim.pensize(10)
#tim.speed(0)
colors = ["teal", "medium slate blue", "lime green", "firebrick", "yellow", "black", "rosy brown", "medium blue"]


# def pick_random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0, 255)

#     random_color = (r, g, b)

#     return random_color

# Creating a square
for _ in range(4):
    tim.forward(100)
    tim.right(90)

# for _ in range(30):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()


# for i in range(3, 11):
#     angle = 360/i
#     tim.color(random.choice(colors))


#    for j in range(i):
#         tim.right(angle)
#         tim.forward(60)

# for _ in range(200):
#     angle = 90 * random.randint(1, 4)
#     tim.color(random.choice(colors))
#     tim.forward(30)
#     tim.right(angle)

# for _ in range(200):
#     angle = 90 * random.randint(1, 4)
#     tim.color(pick_random_color())
#     tim.forward(30)
#     tim.right(angle)

# for _ in range(100):
#     tim.circle(100)
#     tim.color(pick_random_color())
#     tim.right(3.6)

screen = Screen()
screen.exitonclick()
