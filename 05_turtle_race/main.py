import random
from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_game_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


y_position = -100
players = []

if user_bet:
    is_game_on = True

for color in colors:
    player = Turtle(shape="turtle")
    player.penup()
    player.color(color)
    player.goto(x=-230, y=y_position)
    y_position += 40
    players.append(player)


while is_game_on:
    for player in players:
        player.forward(random.randint(0, 10))
        if player.xcor() > 220:
            is_game_on = False
            winner = player.pencolor()
            if winner == user_bet:
                print(f"You guessed! The winner is {winner} ")
            else:
                print(f"You did not guess! The winner was {winner}! ")


screen.exitonclick()
