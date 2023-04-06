from turtle import Screen

from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)
player1 = Paddle()


screen.listen()

screen.onkey(player1.move_up, "Up")
screen.onkey(player1.move_down, "Down")

is_game_on = True
while is_game_on:
    screen.update()



screen.exitonclick()
