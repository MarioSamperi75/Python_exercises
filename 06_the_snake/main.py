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
    # all the segments go on 1 position in the list
    # starting with the last one
    # just the first one change direction
    for i in range(len(segments)-1, 0, -1):
        new_x = segments[i-1].xcor()
        new_y = segments[i-1].ycor()
        segments[i].goto(new_x, new_y)
    segments[0].left(90)
    segments[0].forward(20)

    time.sleep(0.1)


screen.exitonclick()
