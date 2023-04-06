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

while is_game_on:
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_wall()
    if ball.xcor() > 330 and ball.distance(player_r) < 50 or ball.xcor() < - 330 and ball.distance(player_l) < 50:
        ball.bounce_paddle()
    if ball.xcor() > 380:
        print("punto di Player Left!")
        time.sleep(1)
        ball.restart()

    if ball.xcor() < -380:
        print("punto di Player Right!")
        time.sleep(1)
        ball.restart()

    time.sleep(0.0005)



screen.exitonclick()
