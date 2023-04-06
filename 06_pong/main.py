import time
from turtle import Screen

from ball import Ball
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)
player_r = Paddle((350, 0))
player_l = Paddle((-350, 0))
ball = Ball()



screen.listen()

screen.onkey(player_r.move_up, "Up")
screen.onkey(player_r.move_down, "Down")
screen.onkey(player_l.move_up, "w")
screen.onkey(player_l.move_down, "s")

is_game_on = True
x_ball = 0
y_ball = 0
while is_game_on:
    screen.update()
    ball.move()
    time.sleep(0.001)



screen.exitonclick()
