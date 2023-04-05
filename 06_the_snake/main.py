import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
game_is_on = True

for position in starting_positions:
    new_block = Turtle('square')
    new_block.color("white", "white")
    new_block.penup()
    new_block.goto(position)
    segments.append(new_block)



while game_is_on:
    screen.update()
    for seg in segments:
        seg.forward(20)
        time.sleep(0.05)


screen.exitonclick()
