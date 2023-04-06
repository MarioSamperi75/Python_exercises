from turtle import Screen

from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)
player_r = Paddle((350, 0))
player_l = Paddle((-350, 0))


screen.listen()

screen.onkey(player_r.move_up, "Up")
screen.onkey(player_r.move_down, "Down")
screen.onkey(player_l.move_up, "w")
screen.onkey(player_l.move_down, "s")

is_game_on = True
while is_game_on:
    screen.update()


screen.exitonclick()
